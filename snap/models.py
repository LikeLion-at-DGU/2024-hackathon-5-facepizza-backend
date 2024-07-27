from django.db import models
from django.contrib.auth.models import User
import os
from django.core.files.storage import default_storage
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
def image_upload_path(instance, filename):
    return f'{instance.user.username}/{filename}'

EMOTION_CHOICES = [
    ('happy', 'Happy'),
    ('sad', 'Sad'),
    ('angry', 'Angry'),
    ('surprised', 'Surprised'),
    ('disgusted', 'Disgusted'),
    ('fearful', 'Fearful'),
    ('neutral', 'Neutral'),
]

class EmotionImage(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    emotion = models.CharField(max_length=50, choices=EMOTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        # 이미지 파일 삭제
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

# post_delete 신호를 사용하여 모델 인스턴스가 삭제된 후에 파일을 삭제
@receiver(post_delete, sender=EmotionImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)