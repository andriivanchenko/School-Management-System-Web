from django import forms
from tinymce.widgets import TinyMCE
from .models import HomeworkResponses

class HomeworkResponseForm(forms.ModelForm):
    description = forms.CharField(
        widget=TinyMCE(
            attrs={'cols': 80, 'rows': 30},
            mce_attrs={'width': '100%'},
        ),
        label='',
        required=True
    )

    class Meta:
        model = HomeworkResponses
        fields = ['description']