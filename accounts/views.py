from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

import csv
from .forms import TransferForm
from .models import Account, Transaction



def import_accounts(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if not file:
            messages.error(request, 'No file selected. Please choose a file to upload.')
            return redirect('import_accounts')
        
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader)  # Skip header row
        for row in reader:
            account = Account(id=row[0], name=row[1], balance=row[2])
            account.save()
        messages.success(request, 'All data has been successfully imported.')
        return redirect('account_list')
    return render(request, 'accounts/import_accounts.html')


class AccountList(ListView):
    model = Account
    paginate_by = 25


class AccountDetail(DetailView):
    model = Account


def transfer_funds(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            source_account = form.cleaned_data['source_account']
            target_account = form.cleaned_data['target_account']
            amount = form.cleaned_data['amount']
            
            # Check if source account has sufficient balance
            if amount > source_account.balance:
                messages.error(request, 'Transfer amount exceeds source account balance.')
            elif source_account == target_account:
                messages.error(request, 'Source and target accounts cannot be the same.')
            else:
                # Attempt to transfer funds
                try:
                    if source_account.transfer_funds(target_account, amount):
                        messages.success(request, f'Transferred {amount} from {source_account} to {target_account}.')
                        return redirect('transaction_list')
                    else:
                        messages.error(request, 'Failed to transfer funds.')
                except Exception as e:
                    messages.error(request, f'Failed to transfer funds: {str(e)}')
        else:
            messages.error(request, 'Invalid form data. Please check your inputs.')
    else:
        form = TransferForm()

    return render(request, 'accounts/transfer_funds.html', {'form': form})


def get_account_balance(request):
    account_id = request.GET.get('account_id')
    if account_id:
        try:
            account = Account.objects.get(pk=account_id)
            return JsonResponse({'balance': account.balance})
        except Account.DoesNotExist:
            return JsonResponse({'error': 'Account not found'}, status=404)
    return JsonResponse({'error': 'Account ID not provided'}, status=400)


class TransactionList(ListView):
    model = Transaction
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('sender', 'receiver')