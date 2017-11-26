# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Decision(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

class Criteria(models.Model):
    name = models.CharField(max_length=50)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)


class Option(models.Model):
    name = models.CharField(max_length=50)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=62)

class Weight(models.Model):
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)

class Answer(models.Model):
    magnitude = models.IntegerField()
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
