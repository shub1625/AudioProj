from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from .validators import validate_upload_date



class BaseAudio(models.Model):

    duration_time = models.PositiveIntegerField(help_text='Duration in number of seconds')
    uploaded_time = models.DateTimeField(default=datetime.now(),validators=[validate_upload_date])

    class Meta:
        abstract = True

class Song(BaseAudio):
    name = models.CharField(null=False,max_length=100)

    def __str__(self):
        return self.name
    

class Podcast(BaseAudio):
    name = models.CharField(null=False,max_length=100)
    host = models.CharField(null=False,max_length=100)
    participents = ArrayField(models.CharField(max_length=100, blank=True),size=10,null=True,blank=True)

    def __str__(self):
        return self.name
    


class AudioBook(BaseAudio):
    title = models.CharField(null=False,max_length=100)
    author = models.CharField(null=False,max_length=100)
    narrator = models.CharField(null=False,max_length=100)

    def __str__(self):
        return self.title
    

