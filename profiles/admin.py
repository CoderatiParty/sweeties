from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import User_Profile


class User_ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'member_number',
        'get_username',
        'first_name',
        'last_name',
        'get_email',
    )

    readonly_fields = ['get_first_name', 'get_last_name', 'member_number', 'get_username', 'get_email']  # Mark these as readonly in the detail view

    fieldsets = (
        (None, {
            'fields': ('phone_number',)
        }),
        ('User Information', {
            'fields': ('get_first_name', 'get_last_name', 'member_number', 'get_username', 'get_email')
        }),
    )

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username

    get_email.short_description = 'Email'
    get_username.short_description = 'Username'

admin.site.register(User_Profile, User_ProfileAdmin)