from django import forms
from .models import Account

class TransferForm(forms.Form):
    source_account = forms.ModelChoiceField(queryset=Account.objects.all())
    target_account = forms.ModelChoiceField(queryset=Account.objects.all())
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
