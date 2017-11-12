from django.db import models


# Create your models here.
class Decision(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


class Criteria(models.Model):
    name = models.CharField(max_length=50)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    weight = models.IntegerField(min_value=1, max_value=100)


class Option(models.Model):
    name = models.CharField(max_length=50)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=62)


class Answer(models.Model):
    magnitude = models.IntegerField(min_value=1, max_value=10)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
