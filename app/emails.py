import yagmail
from django.urls import reverse


def send_invitation(request, invitation):
    decision = invitation.decision.name
    url = request.build_absolute_uri(reverse('filling', args=[invitation.id]))
    yagmail.SMTP('zenclosure').send(invitation.user.email, "Decisionmaker:" + decision,
                                    "There are decision worth making! <br> You were invited to "
                                    "<a href=\"{url}\">{url}</a> to make a decision.".format(url, url))
