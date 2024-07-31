from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

class Character(models.Model):
    level = models.PositiveIntegerField(default=1, null=False)
    exp = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=False)
    max_exp = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)], null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)