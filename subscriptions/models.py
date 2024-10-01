from django.db import models
from django.utils import timezone

class User_Subscriptions(models.Model):
    type = models.CharField(max_length=12, null=False, blank=False)
    description = models.CharField(max_length=254, null=False, blank=False)
    cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    duration_years = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False)
    duration_days = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    auto_renew = models.BooleanField(default=False, null=True, blank=True)
    purchase_date = models.DateTimeField(null=True, blank=True)
    renew_date = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_description = models.CharField(max_length=254, null=True, blank=True)
    paid = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.type