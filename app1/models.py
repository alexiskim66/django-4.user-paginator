from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    subject = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to="app1/", blank=True, null=True)

    def __str__(self):
        return self.subject

    def summary(self):
        return self.content[:50]

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="app1/")
    image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(60, 30)])

