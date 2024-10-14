from django import forms
from .models import User_Profile
from django.contrib.auth.models import User
from subscriptions.models import User_Subscriptions, Subscription_Info_For_User
from allauth.account.forms import SignupForm
from django.shortcuts import get_object_or_404
from django_countries.fields import CountryField


class UserProfileForm(forms.ModelForm):
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
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False


    def save(self, request):
        user = super().save(request)

        user_profile, created = User_Profile.objects.get_or_create(user=user)

        # Update fields regardless of whether it was created or not
        user_profile.first_name = self.cleaned_data.get('first_name', '')
        user_profile.last_name = self.cleaned_data.get('last_name', '')
        user_profile.phone_number = self.cleaned_data.get('phone_number', '')

        user_profile.save()


        # Now link subscriptions from the session
        cart = request.session.get('cart', {})
        if cart:
            for item_id in cart.keys():
                subscription = get_object_or_404(Subscription_Info_For_User, pk=item_id)
                subscription.user = user_profile  # Link the subscription to the User_Profile
                subscription.save()

        return user
