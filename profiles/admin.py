from django.contrib import admin
from .models import User_Profile


class User_ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'member_number',
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'subscription',
    )


admin.site.register(User_Profile, User_ProfileAdmin)