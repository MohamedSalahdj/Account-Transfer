from django.urls import path

from .views import import_accounts, AccountList, AccountDetail, transfer_funds, get_account_balance, TransactionList

urlpatterns = [
    path('', import_accounts, name='import_accounts'),
    path('list-accounts/', AccountList.as_view(), name='account_list'),
    path('account-detail/<uuid:pk>/', AccountDetail.as_view(), name='account_detail'),
    path('transfer/', transfer_funds, name='transfer_funds'),
    path('get-account-balance/', get_account_balance, name='get_account_balance'),
    path('transaction-list/', TransactionList.as_view(), name='transaction_list'),
]
