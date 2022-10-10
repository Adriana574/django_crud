from django.forms import ModelForm, Textarea
from Cedva1.models import *


class TutorForm(ModelForm):
    class Meta:
        model = Tutor
        fields = "__all__"
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }