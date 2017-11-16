from django.shortcuts import render


def questionnairy_page(request):
    return render(request, 'questionnairy.html')
