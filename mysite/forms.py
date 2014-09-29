from django import forms

class DateForm(forms.Form):
    day = forms.CharField(label='Day', max_length=2)
    month = forms.CharField(label='Month', max_length=2)
