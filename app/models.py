import uuid as uuid
from django.db import models


# Create your models here.
from django.urls import reverse


class Decision(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('decision', args=[str(self.id)])


class Criteria(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    weight = models.IntegerField()


class Option(models.Model):
    name = models.CharField(max_length=50)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=62)


class Invitation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    sent = models.BooleanField(default=False)
    answered = models.BooleanField(default=False)
    uuid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

    def get_absolute_url(self):
        return reverse('filling', args=[str(self.id)])


class Answer(models.Model):
    score = models.IntegerField()
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE)


class WeightedCriteria(models.Model):
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    weight = models.IntegerField()

