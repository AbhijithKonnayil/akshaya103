from django.contrib import admin

from .models import accountsIn, accountsOut, recieptDetails
#bankAccountDetails

admin.site.register(accountsIn)
admin.site.register(accountsOut)
admin.site.register(recieptDetails)
#admin.site.register(bankAccountDetails)
# Register your models here.
