from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=60)
    text=models.TextField()

class PostImage(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   image = models.ImageField(upload_to='image/',blank=True, null=True)
