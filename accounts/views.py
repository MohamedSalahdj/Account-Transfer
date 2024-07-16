from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView

import csv

from .forms import TransferForm
from .models import Account



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


