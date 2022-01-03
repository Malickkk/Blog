from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('post', args=(str(self.id)))
