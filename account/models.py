from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=256)
    username = models.CharField(max_length=64, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name;