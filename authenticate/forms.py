from django import forms 

from .models import UserAccount

class UserAccountCreateForm(forms.ModelForm):

    class Meta:
        model = UserAccount
        fields = ('email', )
    