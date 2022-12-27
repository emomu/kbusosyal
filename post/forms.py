from django import forms
from django.forms import Textarea , ModelForm
from .models import Dweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            
            attrs={
                "placeholder": "hadi bana anlat bir şeyler...",
                "class": "textarea is-warning is-medium", "cols" : 40 , "rows" : 4,

            }
        ),
        label={

            
        }
        )
    liked = forms.CharField( required=False , disabled=True ,
    label ={

    })


    class Meta:
        model = Dweet
        exclude = ('user' , 'tags',)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']




