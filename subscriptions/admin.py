from django.contrib import admin
from .models import User_Subscriptions


class User_SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'subscription_type',
        'description',
        'cost',
        'duration_years',
        'duration_days',
    )


admin.site.register(User_Subscriptions, User_SubscriptionsAdmin)