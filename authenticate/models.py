from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    points = models.IntegerField(default=-1)

    def __str__(self):
        return self.user.username