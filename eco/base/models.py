from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subtitle(models.Model):
    entry_id = models.IntegerField()
    timestamp_vid = models.CharField(max_length=255)
    phrase_vid = models.TextField()

# import os
# os.system('command to execute')
