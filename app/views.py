import json

from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render_to_response

from app.emails import send_invitation
from app.models import Decision, Option, User, Criteria, Invitation


def create(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        decision = data['decision']
        options = data['options']
        criteria = data['criteria']
        emails = data['emails']
        if not decision:
            return bad_request("missing decision name")
        if not options:
            return bad_request("missing options")
        if not criteria:
            return bad_request("missing criteria")
        if not emails:
            bad_request("missing emails")
        decision = Decision.objects.create(name=decision['name'], description=decision['description'])
        users = list(User.objects.get_or_create(email=email)[0] for email in emails)
        options = list(Option.objects.create(name=option, decision=decision) for option in options)
        criteria = list(Criteria.objects.create(name=criterion['name'], weight=criterion['weight'], decision=decision)
                        for criterion in criteria)
        invitations = list(Invitation.objects.create(user=user, decision=decision) for user in users)
        for invitation in invitations:
            send_invitation(invitation)
        return redirect(decision)
    else:
        return HttpResponseNotAllowed(['POST'])


def bad_request(reason=""):
    return HttpResponseBadRequest("400:BAD_REQUEST, reason = {}".format(reason))


def questionnairy_page(request):
    questions = [{'id': 5, 'title': 'question1', 'description': 'description1'},
                 {'id': 2, 'title': 'question2', 'description': 'description2'}]
    options = [{'id': 6, 'title': 'option1'}, {'id': 7, 'title': 'option2'}, {'id': 10, 'title': 'option3'}]
    return render_to_response('questionnairy.html', {'questions': questions, 'options': options})


def decision(request, decision_id):
    decision = Decision.objects.get(id=decision_id)
    invitations = Invitation.objects.filter(decision=decision)
    users = ({"email": invitation.user.email, "link": invitation.get_absolute_url()} for invitation in invitations)
    return render(request=request, template_name="setup_result.html", context={"users": users})


def questionnaire_page(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    return render(request, 'questionnairy.html')


def welcome_page(request):
    return render(request, 'welcome.html')

def result_page(request):
    return render(request, 'result_page.html')

def setup_page(request):
    return render(request, "setup_page.html")