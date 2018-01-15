import yagmail
from django.urls import reverse


def send_invitation(request, invitation):
    decision = invitation.decision.name
    url = request.build_absolute_uri(reverse('filling', args=[invitation.id]))
    yagmail.SMTP('zenclosure').send(invitation.user.email, "Decisionmaker:" + decision,
    "< link rel = \"stylesheet\" href = \"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css\" integrity = \"sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy\" crossorigin = \"anonymous\" >"
    "<div class=\"card\" style=\"width: 40rem;\">"
    "<div class=\"card-body\">"
    "<h5 class=\"card-title\">Decisionmaker</h5>"
    "<p class=\"card-text\">Dear team member: You are invited to take part in a group decision on the topic: <br> {decision} <br> Please click the button to participate:</p>"
    "<a href=\"{url}\" class=\"btn btn-primary\">Participate</a>"
    "</div>"
    "</div>".format(url=url, decision=decision))
                                    # "Dear team member: You are invited to take part in a group decision on the topic: <br> {decision} <br> Please follow the following link:"
                                    # "<a href=\"{url}\">{url}</a> to make a decision.".format(url=url, decision=decision))
