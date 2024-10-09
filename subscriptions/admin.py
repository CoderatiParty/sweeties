from django.contrib import admin
from .models import User_Subscriptions, Subscription_Info_For_User


class User_SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'subscription_type',
        'description',
        'cost',
        'duration_years',
        'duration_days',
    )


admin.site.register(User_Subscriptions, User_SubscriptionsAdmin)


class Subscription_Info_For_UserAdmin(admin.ModelAdmin):
    list_display = (
        'auto_renew',
        'renew_date',
        'paid',
    )


admin.site.register(Subscription_Info_For_User, Subscription_Info_For_UserAdmin)