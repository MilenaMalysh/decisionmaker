# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Decision(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Criteria(models.Model):
    name = models.CharField(max_length=50)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=50)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    leader = models.IntegerField(default=0)
    email = models.CharField(max_length=62)
    def __str__(self):
        return self.first_name

class Weight(models.Model):
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.weight) + " " + str(self.user) + " " + str(self.criteria)

class Answer(models.Model):
    magnitude = models.IntegerField()
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.magnitude) + " " + str(self.criteria) + " " + str(self.option) + " " + str(self.user)
