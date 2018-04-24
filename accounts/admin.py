from django.contrib import admin

from .models import accountsIn, accountsOut, bankAccountDetails, recieptDetail, recieptDetailsOut, bankBalanceDetails,bankRechargeDetails

admin.site.register(accountsIn)
admin.site.register(accountsOut)
admin.site.register(recieptDetail)
admin.site.register(bankAccountDetails)
admin.site.register(recieptDetailsOut)
admin.site.register(bankBalanceDetails)
admin.site.register(bankRechargeDetails)
# Register your models here.
