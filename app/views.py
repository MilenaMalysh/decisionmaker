from django.shortcuts import render, render_to_response


def questionnairy_page(request):
    questions = [{'id': 5, 'title': 'question1', 'description': 'description1'},
                 {'id': 2, 'title': 'question2', 'description': 'description2'}]
    options = [{'id': 6, 'title': 'option1'}, {'id': 7, 'title': 'option2'}, {'id': 10, 'title': 'option3'}]
    return render_to_response('questionnairy.html', {'questions': questions, 'options': options})


def welcome_page(request):
    return render(request, 'welcome.html')
