from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Curr_User(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='users_photo')
    user_info = models.TextField()
    user_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.user_info

    def save(self, **kwargs):
        super().save()

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('user-page')
