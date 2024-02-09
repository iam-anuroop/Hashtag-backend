from django.db import models

class SocialMediaPost(models.Model):
    dateTime = models.DateTimeField()
    content = models.TextField()
    clicks = models.IntegerField()


# Create your models here.
