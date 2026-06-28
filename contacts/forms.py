
from django import forms
from .models import Contact
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\d{10,15}$',
    message='Phone number must contain only digits and be between 10 and 15 digits.'
)

class ContactForm(forms.ModelForm):

    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '📞 Enter Phone Number',
            'maxlength': '15',
            'minlength': '10'
        })
    )

    class Meta:
        model = Contact

        fields = ['name', 'phone', 'email']

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '👤 Enter Full Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '📧 Enter Email '
            }),

        }
