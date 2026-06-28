from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

        widgets = {

            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'👤 Username'
            }),

            'email': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'📧 Email Address'
            }),

        }

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

        self.fields['password1'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'🔒 Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'🔒 Confirm Password'
        })