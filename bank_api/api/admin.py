from django.contrib import admin
from .models import Bank, Branch
# Register your models here.


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('ifsc', 'bank', 'branch', 'address',
                    'city', 'district', 'state')
