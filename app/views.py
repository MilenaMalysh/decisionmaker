from django.shortcuts import render, render_to_response
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest

from app.models import Decision, Option, User, Criteria, Invitation


def create(request):
    if request.method == 'POST':
        decision_name = request.POST['decision']
        options = request.POST['options']
        criteria = request.POST['criteria']
        emails = request.POST['emails']
        if not decision_name:
            return bad_request("missing decision name")
        if not options:
            return bad_request("missing options")
        if not criteria:
            return bad_request("missing criteria")
        if not emails:
            bad_request("missing emails")
        decision = Decision.objects.create(name=decision_name, description="")
        users = (User.objects.get_or_create(email=email) for email in emails)
        options = (Option.objects.create(name=option, decision=decision) for option in options)
        criteria = (Criteria.objects.create(name=criterion['name'], decision=decision) for criterion in criteria)
        invitations = (Invitation.objects.create(user=user, decision=decision) for user in users)
    else:
        return HttpResponseNotAllowed(['POST'])


def bad_request(reason=""):
    return HttpResponseBadRequest("400:BAD_REQUEST, reason = {}".format(reason))


def questionnairy_page(request):
    questions = [{'id': 5, 'title': 'question1', 'description': 'description1'},
                 {'id': 2, 'title': 'question2', 'description': 'description2'}]
    options = [{'id': 6, 'title': 'option1'}, {'id': 7, 'title': 'option2'}, {'id': 10, 'title': 'option3'}]
    return render_to_response('questionnairy.html', {'questions': questions, 'options': options})


def welcome_page(request):
    return render(request, 'welcome.html')

def result_page(request):
    return render(request, 'result_page.html')

def setup_page(request):
    return render(request, "setup_page.html")