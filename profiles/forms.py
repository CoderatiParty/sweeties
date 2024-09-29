from django import forms
#from .models import User_Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = User_Profile
#        exclude = ('user', 'member_number')

#    def __init__(self, *args, **kwargs):
#         """
#        Add placeholders and classes, remove auto-generated
#        labels and set autofocus on first field
#        """
#        super().__init__(*args, **kwargs)
#        placeholders = {
#            'first_name': 'First Name',
#            'last_name': 'Last Name',
#            'street_address1': 'Street Address 1',
#            'street_address2': 'Street Address 2',
#            'town_or_city': 'Town or City',
#            'county': 'County, State or Locality',
#            'post_or_zipcode': 'Postal Code',
#            'country': 'Country',
#            'phone_number': 'Phone Number',
#            'email': 'Email',
#        }
#
#        self.fields['phone_number'].widget.attrs['autofocus'] = True
#        for field in self.fields:
#            if field != 'country':
#                if self.fields[field].required:
#                    placeholder = f'{placeholders[field]} *'
#                else:
#                    placeholder = placeholders[field]
#                self.fields[field].widget.attrs['placeholder'] = placeholder
#            self.fields[field].widget.attrs['class'] = ('border-black '
#                                                        'rounded-0 '
#                                                        'profile-form-input')
#            self.fields[field].label = False


class CustomForm(forms.Form):
    name = forms.CharField(label="Your Name")
    email = forms.EmailField(label="Your Email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
            Field('email'),
            Submit('submit', 'Submit')
        )
        self.helper.form_method = 'POST'