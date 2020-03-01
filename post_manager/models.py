from django.db import models
from django.conf import settings
from django.utils import timezone

from django.db.models.signals import post_save

from authenticate.models import UserAccount

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return "/post"

    def __str__(self):
        return self.title 

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(default=timezone.now)

class Like(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

def increment_points(sender, instance, created, *args, **kwargs):
    points = Comment.objects.all().filter(post_id=instance.post_id.pk)
    author = Post.objects.get(pk=instance.post_id.pk).author
    print(author)
    print(author.pk)
    user_account = UserAccount.objects.get(user=author)
    # give em some points 

post_save.connect(increment_points, sender=Comment)