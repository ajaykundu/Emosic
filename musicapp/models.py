from django.db import models

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

Emotions = ['fear','contempt','anger','sadness','surprise','neutral','disgust','happiness']

# Create your models here.
class Song(model.Model):
    name = model.CharField(max_length=125)
    audio_file = model.FileField(upload_to='SongsFolder')
    emotionAttached = models.CharField(max_length=6, choices=Emotions, default='green')
