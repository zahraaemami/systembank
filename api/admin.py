from django.contrib import admin

from .models import Branch,Bank,Client,ClientManager,Account,Transfer,Withraw,Deposit


class BranchAdmin(admin.ModelAdmin) :

    list_display = ('name' ,'address')
    search_fields= ('name',)

admin.site.register(Branch,BranchAdmin) 


class BankAdmin(admin.ModelAdmin) :
    list_display = ('name', 'branch')
    search_fields = ('name',)

admin.site.register(Bank,BankAdmin)   


class ClientAdmin(admin.ModelAdmin) :
    list_display = ('name', 'address')
    search_fields = ('name',)

admin.site.register(Client,ClientAdmin)


class ClientManagerAdmin(admin.ModelAdmin) :
    list_display = ('name' , 'address')
    search_fields=('name','address')

admin.site.register(ClientManager,ClientManagerAdmin)    


class AccountAdmin(admin.ModelAdmin) :
    list_display = ('client','bank','open_data','account_type')
    search_fields = ('account_type',)

admin.site.register(Account,AccountAdmin)



class TransferAdmin(admin.ModelAdmin) :
    list_display = ('account','branch','transaction_data','status')
    search_fields = ('account','status')

admin.site.register(Transfer,TransferAdmin)


class WithrawAdmin(admin.ModelAdmin) :

    list_display = ('ammount','account','transaction_data','status')
    search_fields = ('ammount' ,'account')

admin.site.register(Withraw,WithrawAdmin)


class DepositAdmin(admin.ModelAdmin):
    list_display = ('ammount','account','transaction_data', 'status')
    search_fields = ('account','status')

admin.site.register(Deposit,DepositAdmin)