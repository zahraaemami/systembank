from rest_framework import serializers

from .models import Branch,Bank,Client,ClientManager,Account,Transfer,Withraw,Deposit

class BranchSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Branch
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Bank
        fields = '__all__'        


class ClientSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Client
        fields = '__all__'



class ClientManagerSerializer(serializers.ModelSerializer) :

    class Meta :
        model = ClientManager
        fields = '__all__'


class AccountSerializer (serializers.ModelSerializer) :
    
    class Meta :

        model = Account
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer) :

    class Meta :
        model  = Transfer
        fields = '__all__'


class WithrawSerializer(serializers.ModelSerializer) :

    class Meta :

        model = Withraw
        fields = '__all__'



class DepositSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Deposit
        fields = '__all__'


