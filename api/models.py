from __future__ import unicode_literals

from django.db import models




class Branch (models.Model) :

    name  = models.CharField(max_length = 150)
    address  = models.CharField(max_length = 150)
    branch_code  = models.CharField(max_length = 150)

    class Meta :
        verbose_name_plural = "Branches"

    def json_object (self) :

        return {
                "name" : self.name ,
                "address" : self.address ,
                "branch_code" : self.branch_code
            }

    def __str__(self) :
            return self.name


class Bank (models.Model) :
    name  = models.CharField(max_length = 150)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def json_object (self) :
        return {
        "name" :self.name ,
        "branch" : self.branch
        }

    def __str__(self) :
        return self.name



class ClientManager (models.Model) :
    name  = models.CharField(max_length = 150)
    address  = models.CharField(max_length = 150)

    def __str__(self) :
        return self.name



class Client(models.Model) :

    name  = models.CharField(max_length = 150)
    address  = models.CharField(max_length = 150)

    def json_object (self) :
        return {
            "name" :self.name ,
            "address" :self.address
        }

    def __str__(self) :
        return self.name



class Account(models.Model) :

    """Represents Bank Account"""

    client  = models.ForeignKey(Client, on_delete=models.CASCADE)
    open_data  = models.DateTimeField( auto_now_add=True)
    account_type  = models.CharField(max_length = 250)
    bank  = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def json_object (self) :
        return {
        "open_data" :self.open_data ,
        "account_type" : self.account_type ,
        "bank" : self.bank.name
        }

    def __str__(self) :
        return self.account_type


class Transfer(models.Model) :
    
    account = models.ForeignKey(Account , on_delete= models.CASCADE)
    branch  = models.ForeignKey(Branch, on_delete=models.CASCADE)
    transaction_data  = models.DateTimeField(auto_now_add = True)
    status  = models.CharField(max_length = 150 , choices =[('success' ,'Success') , ('failed','Failed')] , default = 'success')

    

    def json_object (self) :

        return {
            "account" : self.account.account_number ,
            "branch" : self.branch.name
        }

    def __str__(self) :

        return "account Transfrred to {}Branch".format(self.branch.name)
    
    
    

class Withraw(models.Model) :

    ammount = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_data  = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 150, choices = [('success','Succes') , ('failed', 'Failed')] , default = 'success')
    

class Deposit (models.Model) :

    ammount = models.FloatField()
    account = models.ForeignKey(Account , on_delete = models.CASCADE)
    transaction_data = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length = 150 , choices =[('success' ,'Success') ,('failed', 'Failed')] , default = 'success')
        
    
    
    
    
