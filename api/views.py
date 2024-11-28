from __future__ import unicode_literals
from rest_framework import serializers
from rest_framework import status , generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response
from rest_framework import viewsets
from .models import (
    Branch ,Bank, Client,ClientManager , 
    Account , Transfer ,
     Withraw, Deposit)

from .serializers import (
    BranchSerializer,BankSerializer,
    ClientSerializer , ClientManagerSerializer,
    AccountSerializer , TransferSerializer ,
    WithrawSerializer, DepositSerializer
)

class BranchAPIView(generics.ListCreateAPIView) :

    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BanksAPIView(generics.ListCreateAPIView) :
        queryset = Bank.objects.all()
        serializer_class = BankSerializer

class ClientViewSet(viewsets.ModelViewSet) :

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientManagerViewSet(viewsets.ModelViewSet) :

    queryset = ClientManager.objects.all()
    serializer_class = ClientManagerSerializer


# class AccountViewSet(viewsets.ModelViewSet) :

#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer


class TransferViewSet(viewsets.ModelViewSet) :

    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class WithrawViewSet(viewsets.ModelViewSet) :

    queryset = Withraw.objects.all()
    serializer_class = WithrawSerializer


class DepositViewSet(viewsets.ModelViewSet) :

    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class AccountAPIView(generics.ListAPIView) :

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    