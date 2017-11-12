from django.shortcuts import render

import settings


def questionnairy_page(request):
    print(settings.STATICFILES_DIRS)
    return render(request, 'questionnairy.html')
