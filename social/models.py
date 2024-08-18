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

    def __str__(self):
        return (
            f"{self.body} "
            f"{self.user} "
            f"{self.created:%Y-%m-%d %H:%M}"
            )
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # if user is deleted, profile is deleted
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='img/')

    def __str__(self):
        return self.user.username
    
# @receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        user_profile.follows.set([ instance.profile.id ])

post_save.connect(createProfile, sender=User)