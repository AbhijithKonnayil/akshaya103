from django.contrib import admin

from .models import accountsIn, accountsOut, bankAccountDetails, recieptDetail

admin.site.register(accountsIn)
admin.site.register(accountsOut)
admin.site.register(recieptDetail)
admin.site.register(bankAccountDetails)
# Register your models here.
