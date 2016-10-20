from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author=models.ForeignKey(User)
    title=models.TextField()
    text=models.TextField()
    created_data=models.DateTimeField(default=timezone.now)
    published_data=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_data=timezone.now()
        self.save()

    def __str__(self):
        return  self.title.encode('utf-8')


