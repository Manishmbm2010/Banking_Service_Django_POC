from django.contrib import admin

from .models import BankCustomer ,BankAccount , CreditTransfer

admin.site.register(BankCustomer)
admin.site.register(BankAccount)
admin.site.register(CreditTransfer)