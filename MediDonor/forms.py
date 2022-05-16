from .models import Organ, nominee, post
from django import forms


class DonateForm(forms.ModelForm):
    class Meta:
        model = Organ
        fields = ['blood_group', 'organ_age', 'organ_type']


class NomineeForm(forms.ModelForm):
    class Meta:
        model = nominee
        fields = ['nominee_name', 'nominee_mobile', 'nominee_email', 'relation']


class DateInput(forms.DateInput):
    input_type = 'date'


class PostingForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'location', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }
