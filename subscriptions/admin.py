from django.contrib import admin
from .models import User_Subscriptions


class User_SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'description',
        'cost',
        'duration_years',
        'duration_days',
        'auto_renew',
        'purchase_date',
        'renew_date',
        'paid',
    )


admin.site.register(User_Subscriptions, User_SubscriptionsAdmin)