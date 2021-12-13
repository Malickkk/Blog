from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=(str(self.id)))
