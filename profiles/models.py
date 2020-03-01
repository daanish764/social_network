from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=130, null=True, blank=True)
    picture = models.ImageField(upload_to="videos/", null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def calculate(self):
        return str(self.user) + " in " + str(self.location)


    def get_absolute_url(self):
        url = reverse("profile:index", kwargs={"username": self.user.username})
        return url
