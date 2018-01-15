import os
import yagmail
from django.urls import reverse


def send_invitation(request, invitation):
    decision = invitation.decision.name
    url = request.build_absolute_uri(reverse('filling', args=[invitation.id]))
    password = os.getenv('EMAIL_PASSWORD')
    yagmail.SMTP('zenclosure', password).send(invitation.user.email, "Decisionmaker:" + decision,
                                    "There are decision worth making! <br> You were invited to "
                                    "<a href=\"{url}\">{url}</a> to make a decision.".format(url=url))
