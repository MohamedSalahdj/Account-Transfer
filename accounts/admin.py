from django.contrib import admin
from .models import Account, Transaction



class CustomiseAccount(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Account, CustomiseAccount)
admin.site.register(Transaction)