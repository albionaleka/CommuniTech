from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(
        User, related_name="tweets", on_delete=models.DO_NOTHING
    )

    body = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name="tweet_like", blank=True)

    image = models.ImageField(upload_to='img/', blank=True, null=True)

    title = models.CharField(max_length=50, null=False, blank=False, default="Post title")

    def like_tracker(self):
        return self.likes.count()

    def __str__(self):
        return (
            f"{self.title}"
            f"{self.image}"
            f"{self.body} "
            f"{self.user} "
            f"{self.created:%Y-%m-%d %H:%M}"
            )
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # if user is deleted, profile is deleted
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='img/')

    profile_bio = models.CharField(blank=True, null=True, max_length=300)
    facebook = models.CharField(blank=True, null=True, max_length=100)
    linkedin = models.CharField(blank=True, null=True, max_length=100)
    instagram = models.CharField(blank=True, null=True, max_length=100)
    homepage = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        user_profile.follows.set([ instance.profile.id ])

post_save.connect(createProfile, sender=User)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Tweet, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.body}