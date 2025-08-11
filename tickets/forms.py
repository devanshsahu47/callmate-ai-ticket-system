from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['customer_name', 'email', 'description', 'urgency']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your issue',
                'rows': 4,
                'required': True,
            }),
            'urgency': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'required': True,
            }),
        }
