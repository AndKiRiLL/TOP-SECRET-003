from django import forms
from .models import Course, Student

class FormCreate(forms.Form):
    name = forms.CharField(max_length=30, required=True, label='', widget=forms.TextInput(attrs={'name': 'name'}))

    courses = Course.objects.all().values_list()
    course = forms.BooleanField(required=True, label='', widget=forms.CheckboxSelectMultiple(choices=courses, attrs={'name': 'courses'}))