import yagmail
from django.urls import reverse


def send_invitation(request, invitation):
    decision = invitation.decision.name
    url = request.build_absolute_uri(reverse('filling', args=[invitation.id]))
    yagmail.SMTP('zenclosure').send(invitation.user.email, "Decisionmaker:" + decision,
                                    "<div style=\"width: 40rem; border: 1px solid rgb(0, 128, 128); border-radius: 5px\">"
                                    "<h3 style=\"background-color: rgb(0, 128, 128); margin: 0; padding: 10px; text-align: center; color: white; font: 15px arial, sans-serif;\">Decisionmaker</h3>"
                                    "<p style=\"text-align: center;\">Dear team member: You are invited to take part"
                                    "in a group decision on the topic: <br><b> \"{decision}\"</b> <br> Please click the "
                                    "button to participate:</p>"
                                    "<a style=\"display:block; text-align: center\" href=\"{url}\">"
                                    "<button style=\"background-color: rgb(0, 128, 128); border-radius: 5px; border:none; color:white; padding: 5px 10px 5px 10px; margin-bottom: 10px\">Participate</button>"
                                    "</a>"
                                    "</div>".format(url=url, decision=decision))
