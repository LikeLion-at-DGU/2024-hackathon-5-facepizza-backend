# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# class EmotionRecord(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     emotion = models.CharField(max_length=100)
#     score = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.first_name} : {self.emotion} ({self.score})"

# stretching/models.py
from django.db import models
from django.contrib.auth.models import User

class ExerciseRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content} - {self.date}"
