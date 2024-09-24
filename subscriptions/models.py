from django.db import models

class User_Subscriptions(models.Model):
    type = models.CharField(max_length=12, null=False, blank=False)
    description = models.CharField(max_length=254, null=False, blank=False)
    cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    duration = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False)


    def __str__(self):
        return self.type