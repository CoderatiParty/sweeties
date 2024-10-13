import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal
from profiles.models import User_Profile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(User_Profile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    subscription = models.ForeignKey('subscriptions.User_Subscriptions', null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    lineitem_total = models.DecimalField(max_digits=4, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)
    
    def save(self, *args, **kwargs):
        """
        Override the save method to calculate the lineitem total.
        """
        # Calculate lineitem total: subscription cost * quantity
        self.lineitem_total = self.subscription.cost * Decimal(self.quantity)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.subscription.subscription_type} Subscription on order {self.order.order_number}'