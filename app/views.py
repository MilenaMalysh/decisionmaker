from django.shortcuts import render


def test_template_static(request):
    return render(request, "test_template.html", {'title': 'MyTitle', 'text': "MyText"})
