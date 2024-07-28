# Generated by Django 5.0.7 on 2024-07-27 15:34

import django.db.models.deletion
import tracking.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('happy', models.FloatField(default=0)),
                ('sad', models.FloatField(default=0)),
                ('angry', models.FloatField(default=0)),
                ('surprised', models.FloatField(default=0)),
                ('disgusted', models.FloatField(default=0)),
                ('fearful', models.FloatField(default=0)),
                ('neutral', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('memo', models.TextField(max_length=200, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to=tracking.models.HighlightImage_upload_path)),
                ('emotion', models.CharField(choices=[('happy', 'Happy'), ('sad', 'Sad'), ('angry', 'Angry'), ('surprised', 'Surprised'), ('disgusted', 'Disgusted'), ('fearful', 'Fearful'), ('neutral', 'Neutral')], max_length=10)),
                ('report_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.report')),
            ],
        ),
    ]