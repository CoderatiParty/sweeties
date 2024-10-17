from django import forms
from .models import User_Profile
from django.contrib.auth.models import User
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from allauth.account.forms import SignupForm
from django.shortcuts import get_object_or_404
from django_countries.fields import CountryField


class UserProfileForm(forms.ModelForm):
    """
    Function for user form data
    """
    class Meta:
        model = User_Profile
        fields = ('first_name', 'last_name', 'phone_number', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'email': 'Email',
        }

        for field in self.fields:
            if field != 'user' and field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders.get(field, field.capitalize())} *'
                else:
                    placeholder = placeholders.get(field, field.capitalize())
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['aria-label'] = placeholders.get(field, field.capitalize())
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False

    def save(self, commit=True, user=None):
        """ Ensure user is passed to the form when saving """
        profile = super().save(commit=False)
        if user:
            profile.user = user  # Set the user explicitly
        if commit:
            profile.save()
        return profile


class CustomSignupForm(SignupForm):
    """
    Function for custom signup form setup
    """
    first_name = forms.CharField(max_length=80, required=True)
    last_name = forms.CharField(max_length=80, required=True)
    phone_number = forms.CharField(max_length=20, required=True)


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'email': 'Email',
            'email2': 'Confirm Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['aria-label'] = placeholders.get(field, field.capitalize())
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False


    def save(self, request):
        user = super().save(request)

        # Update the email field in the User model
        user.email = self.cleaned_data.get('email', '')
        user.save()

        # Create or update the user's profile
        user_profile, created = User_Profile.objects.get_or_create(user=user)

        # Update fields in profile
        user_profile.first_name = self.cleaned_data.get('first_name', '')
        user_profile.last_name = self.cleaned_data.get('last_name', '')
        user_profile.phone_number = self.cleaned_data.get('phone_number', '')
        user_profile.email = user.email

        user_profile.save()

        # Link subscriptions from the session cart
        cart = request.session.get('cart', {})
        if cart:
            for item_id in cart.keys():
                # Retrieve the actual User_Subscriptions object (or the correct model)
                subscription = get_object_or_404(User_Subscriptions, pk=item_id)

                # Now create or update Subscription_Info_For_User
                Subscription_Info_For_User.objects.get_or_create(
                    user_profile=user_profile,
                    subscription=subscription,
                    defaults={'auto_renew': cart[item_id].get('auto_renew', False)}
                )

        return user