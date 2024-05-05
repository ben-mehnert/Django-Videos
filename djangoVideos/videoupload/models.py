from django.db import models
from django.core.validators import FileExtensionValidator

def default_thumbnail():
    return 'thumbnails/default_thumbnail.jpg'

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Video(models.Model):
    name = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='media/', unique=True, validators=[FileExtensionValidator(['mp4'])])
    tags = models.ManyToManyField(Tag)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)

    def __str__(self):
        return self.name
