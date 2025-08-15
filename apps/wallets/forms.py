from django import forms
from django.core.validators import RegexValidator


class WalletAddressForm(forms.Form):
    address = forms.CharField(
        max_length=42,
        min_length=42,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '0x112532B200980Ddee8226023bEbBE2E6884C31e2',
            'autocomplete': 'off',
        }),
        validators=[
            RegexValidator(
                regex=r'^0x[a-fA-F0-9]{40}$',
                message='Please enter valid Ethereum wallet address.'
            )
        ],
        label="Enter wallet address",
    )