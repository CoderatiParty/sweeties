from django.contrib import admin
from .models import User_Subscriptions


class User_SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'description',
        'cost',
        'duration',
    )


admin.site.register(User_Subscriptions, User_SubscriptionsAdmin)