from django.contrib import admin

# Register your models here.
from app import models

admin.site.register([models.Decision, models.Invitation, models.Option, models.Criteria, models.Answer, models.User])
