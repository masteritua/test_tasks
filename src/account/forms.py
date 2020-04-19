from django import forms
from django.contrib.admin import widgets
from account.models import User, Profile
from bootstrap_datepicker.widgets import DatePicker
import socket


class ProfileEdit(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(ProfileEdit, self).__init__(*args, **kwargs)

        user = kwargs.get('instance')
        profile = Profile.objects.get(user_id=user.id)

        self.fields['date_of_birth'].initial = profile.date_of_birth
        self.fields['biography'].initial = profile.biography
        self.fields['contacts'].initial = profile.contacts

    date_of_birth = forms.DateField(
        widget=DatePicker(
            options={
                "format": "yyyy-mm-dd",
                "autoclose": True
            }
        )
    )

    biography = forms.CharField(widget=forms.Textarea(), required=False)
    contacts = forms.CharField(widget=forms.Textarea(), required=False)
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'biography', 'contacts', 'date_of_birth')

    def clean(self):
        cleaned_data = super().clean()

        if not self.errors:

            if cleaned_data['password'] and cleaned_data['password2']:

                if cleaned_data['password'] != cleaned_data['password2']:
                    raise forms.ValidationError('Passwords do not match!')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)  # no save to database
        user.set_password(self.cleaned_data['password'])  # password should be hashed!
        user.save(update_fields=['password', 'email', 'first_name', 'last_name'])

        profile = Profile.objects.get(user_id=user.id)
        profile.ip = socket.gethostbyname(socket.gethostname())
        profile.biography = self.cleaned_data['biography']
        profile.contacts = self.cleaned_data['contacts']
        profile.date_of_birth = self.cleaned_data['date_of_birth']
        profile.save(update_fields=['biography', 'contacts', 'date_of_birth', 'ip'])

        return user
