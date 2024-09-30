from django.db import models
from django.contrib.auth.models import User  # Импорт модели User

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="videos/thumbnails")
    source = models.FileField(upload_to="videos")

    def __str__(self):
        return str(self.id) + " - " + self.title


class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.video.title}"