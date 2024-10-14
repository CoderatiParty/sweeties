from django.contrib import admin
from .models import User_Profile


class User_ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'member_number',
        'get_username',
        'first_name',
        'last_name',
        'get_email',
    )

    readonly_fields = ['member_number']  # Only actual model fields should be here

    fieldsets = (
        (None, {
            'fields': ('phone_number',)
        }),
        ('User Information', {
            # Only model fields are allowed in fieldsets
            'fields': ('first_name', 'last_name', 'member_number')
        }),
    )

    # Custom methods to display related user information in list_display
    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username
    
    # Ensuring the user object is refreshed from the database
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj and obj.user:
            obj.user.refresh_from_db()

        return super().change_view(request, object_id, form_url, extra_context)
    
    # Override the save_model method to update the User model as well
    def save_model(self, request, obj, form, change):
        """
        When saving the User_Profile, also save changes to the related User model.
        """
        user = obj.user
        # Update the User model fields based on the User_Profile form data
        user.first_name = form.cleaned_data.get('first_name', user.first_name)
        user.last_name = form.cleaned_data.get('last_name', user.last_name)
        user.email = form.cleaned_data.get('email', user.email)
        user.save()  # Save the updated User instance
        
        super().save_model(request, obj, form, change)  # Save the User_Profile instance


    # Short descriptions for the list_display
    get_email.short_description = 'Email'
    get_username.short_description = 'Username'

# Register the User_Profile model with the custom admin class
admin.site.register(User_Profile, User_ProfileAdmin)