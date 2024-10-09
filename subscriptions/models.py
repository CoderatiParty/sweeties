from django.db import models
from django.utils import timezone
from profiles.models import User_Profile


class User_Subscriptions(models.Model):
    subscription_type = models.CharField(max_length=12, null=False, blank=False)
    description = models.CharField(max_length=254, null=False, blank=False)
    cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    duration_years = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False)
    duration_days = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.subscription_type
    

class User_Subscription_Info_For_User(models.Model):
    auto_renew = models.BooleanField(default=False, null=True, blank=True)
    purchase_date = models.DateTimeField(null=True, blank=True)
    renew_date = models.DateTimeField(null=True, blank=True)
    paid = models.BooleanField(default=False, null=True, blank=True)
    user_profile = models.ForeignKey(User_Profile, on_delete=models.CASCADE, related_name='subscription_info')
    subscription = models.ForeignKey(User_Subscriptions, on_delete=models.CASCADE, related_name='subscription_chosen')

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.subscription.subscription_type}"