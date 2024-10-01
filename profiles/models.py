import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from subscriptions.models import User_Subscriptions


class User_Profile(models.Model):
    """
    A model for maintaining user's details, subscription information and history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=80,
                                               null=True, blank=True)
    first_name = models.CharField(max_length=80,
                                               null=True, blank=True)
    last_name = models.CharField(max_length=80,
                                               null=True, blank=True)
    member_number = models.BigIntegerField(unique=True, editable=False)
    phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    email = models.CharField(max_length=80,
                                               null=True, blank=True)
    subscription = models.ForeignKey(User_Subscriptions, 
                                     on_delete=models.SET_NULL, 
                                     null=True, blank=True)

    def __str__(self):
        return self.user.username
    

    def save(self, *args, **kwargs):
        if not self.member_number:
            self.member_number = random.randint(100000000, 999999999)  # Random 9-digit number
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        User_Profile.objects.create(user=instance)
    else:
        # Existing users: Save the profile only if it has been modified
        instance.user_profile.save()
