from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=20, null=False)
    level = models.PositiveIntegerField(default=1, null=False)
    experience = models.PositiveIntegerField(default=0, 
                                             validators=[MaxValueValidator(100)], null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)