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
from django.views.generic import RedirectView

from app import views

urlpatterns = [
    url(r'^decision/setup', views.setup_decision, name='decision_setup'),
    url(r'^decision/create$', views.create, name='decision_create'),
    url(r'^decision/(?P<decision_id>\d+)/$', views.decision, name='decision'),
    url(r'^filling/(?P<invitation_id>\d+)/$', views.filling_page, name='filling'),
    url(r'^submit/(?P<invitation_id>\d+)/$', views.submit, name='submit'),
    url(r'^result/(?P<invitation_id>\d+)/$', views.result_page, name='decision_result'),
    url(r'^decision/(?P<decision_id>\d+)/result/$', views.result_plain, name='decision_result_plain'),
    url(r'^invitation/(?P<invitation_id>\d+)/accepting$', views.accept_result, name='accept_result'),
    url(r'^index/', views.landing, name='index'),
    url(r'^thank_you/', views.thank_you, name='thank_you'),
    url(r'^', RedirectView.as_view(pattern_name='index', permanent=False)),
]
