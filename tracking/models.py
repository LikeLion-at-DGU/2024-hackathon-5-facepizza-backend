from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def HighlightImage_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

EMOTION_CHOICES = [
    ('happy', 'Happy'),
    ('sad', 'Sad'),
    ('angry', 'Angry'),
    ('surprised', 'Surprised'),
    ('disgusted', 'Disgusted'),
    ('fearful', 'Fearful'),
    ('neutral', 'Neutral'),
]

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    happy = models.FloatField(default=0)
    sad = models.FloatField(default=0)
    angry = models.FloatField(default=0)
    surprised = models.FloatField(default=0)
    disgusted = models.FloatField(default=0)
    fearful = models.FloatField(default=0)
    neutral = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)                  # 시간도 출력?
    # updated_at = models.DateTimeField(auto_now=True)                    # 필요?
    memo = models.TextField(max_length=200, null=True)

class Highlight(models.Model):
    id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(Report, null=False, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=HighlightImage_upload_path, null=True)    # 하이라이트 몇 장씩 출력할건지?
    emotion = models.CharField(max_length=10, choices=EMOTION_CHOICES)                      