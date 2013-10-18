from django import forms
from lwimw.models import *

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = ('contest', 'user')


