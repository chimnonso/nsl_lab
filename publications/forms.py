from django import forms
from .models import Journal

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        # fields = '__all__'  # You can specify the fields you want to include in the form
        exclude = ['writer', 'write_date', 'update_date', 'ack', 'visit']


class JournalUpdateForm(forms.ModelForm):
    class Meta:
        model = Journal
        # fields = '__all__'  # You can specify the fields you want to include in the form
        exclude = ['write_date', 'update_date', 'visit']

        # widgets = {
        #     'ack': forms.TextInput(attrs={'required': False}),
        # }