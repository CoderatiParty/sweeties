from django.contrib import admin
from .models import User_Profile


class User_ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'member_number',
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'post_or_zipcode',
        'country',
    )


admin.site.register(User_Profile, User_ProfileAdmin)