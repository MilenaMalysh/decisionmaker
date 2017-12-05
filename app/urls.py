"""decisionmaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^questionnaire/create$', views.create, name='create'),
    url(r'^decision/(?P<decision_id>.*)/$', views.decision, name='decision'),
    url(r'^filling/(?P<invitation_id>.*)/$', views.questionnaire_page, name='questionnaire'),
    url(r'^result', views.result_page, name='result'),
    url(r'^welcome', views.welcome_page, name='welcome_page'),
    url(r'^setup', views.setup_page, name='setup_page'),
    url(r'^', views.welcome_page, name='welcome_page'),
]
