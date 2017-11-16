from django.shortcuts import render

import settings


def questionnairy_page(request):
    return render(request, 'questionnairy.html')
