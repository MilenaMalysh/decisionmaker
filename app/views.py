import json

from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render_to_response
from django.urls import reverse

from app.emails import send_invitation
from app.models import Decision, Option, User, Criteria, Invitation, Answer, WeightedCriteria
from app.decision import group_solution, normal_solution


def create(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        decision = data['decision']
        options = data['options']
        criteria = data['criteria']
        emails = (user['email'] for user in data['users'])
        if not decision:
            return bad_request("missing decision name")
        if not options:
            return bad_request("missing options")
        if not criteria:
            return bad_request("missing criteria")
        if not emails:
            bad_request("missing emails")
        decision = Decision.objects.create(name=decision)
        users = list(User.objects.get_or_create(email=email)[0] for email in emails)
        options = list(Option.objects.create(name=option['title'], decision=decision) for option in options)
        criteria = list(Criteria.objects.create(name=criterion['title'], description=criterion['description'],
                                                weight=criterion['weight'], decision=decision)
                        for criterion in criteria)
        invitations = list(Invitation.objects.create(user=user, decision=decision) for user in users)
        for invitation in invitations:
            send_invitation(invitation)
        return JsonResponse({'redirect': decision.get_absolute_url()})
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


def filling_page(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    options = ({'id': option.id, 'title': option.name}
               for option in Option.objects.filter(decision=invitation.decision))
    criteria = ({'id': criterion.id, 'title': criterion.name, 'description': criterion.description}
                for criterion in Criteria.objects.filter(decision=invitation.decision))
    return render(request=request, template_name='questionnairy.html',
                  context={'options': list(options), 'questions': list(criteria), 'invitation_id': invitation.id})


def landing(request):
    return render(request, 'welcome.html')


def result_page(request, decision_id, invitation_id):
    decision = Decision.objects.get(id=decision_id)
    finished = all(decision.answered for decision in Invitation.objects.filter(decision=decision))
    if finished:
        group_result = group_solution(decision)
        normal_result = normal_solution(decision)
        return render(request, 'result_page.html',
                      {'invitation_id': invitation_id,
                       'group_result': group_result.name,
                       'normal_result': normal_result.name})
    return render(request, 'result_page.html')


def setup_decision(request):
    return render(request, "setup_page.html")


def submit(request, invitation_id):
    if request.method == 'POST':
        invitation = Invitation.objects.get(id=invitation_id)
        if invitation.answered:
            return HttpResponseBadRequest("already answered")
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        answers = data['answers']
        for answer in answers:
            criteria = Criteria.objects.get(id=answer['question_id'])
            weighted_criteria = WeightedCriteria.objects.create(criteria=criteria,
                                                                invitation=invitation,
                                                                weight=answer['weight'])
            for option_score in answer['options']:
                score = Answer.objects.create(criteria=criteria, invitation=invitation, score=option_score['score'],
                                              option=Option.objects.get(id=option_score['option_id']))
        invitation.answered = True
        invitation.save()
        return JsonResponse({'redirect': reverse("decision_result", args=[invitation.decision.id])})
    else:
        return HttpResponseNotAllowed(['POST'])
