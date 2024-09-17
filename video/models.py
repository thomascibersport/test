from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="videos/thumbnails")
    source = models.FileField(upload_to="videos")

    def __str__(self):
        return str(self.id) + " - " + self.title
