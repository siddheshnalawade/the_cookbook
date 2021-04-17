from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    display_image = models.CharField(max_length=500)

    def __str__(self):
        return self.title+' by '+self.author