from django.urls import path

from .views import import_accounts, AccountList, AccountDetail

urlpatterns = [
    path('import-accounts/', import_accounts, name='import_accounts'),
    path('list-accounts/', AccountList.as_view(), name='list_accounts'),
    path('account-detail/<uuid:pk>/', AccountDetail.as_view(), name='account_detail'),

]
