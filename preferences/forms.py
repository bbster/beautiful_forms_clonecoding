from django import forms
from .models import Preference
from django.core.exceptions import ValidationError


class PreferenceModelForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = '__all__'

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) < 10:
            raise ValidationError('the bio is too short')
        return bio

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 10:
            raise ValidationError('the first_name is too short')
        return first_name
