from django.urls import path ,include

from .views import (
    BanksAPIView ,
    BranchAPIView,
    ClientViewSet,
    ClientManagerViewSet,AccountViewSet ,
    TransferViewSet ,WithrawViewSet,
    DepositViewSet
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients',ClientViewSet)
router.register(r'managers',ClientManagerViewSet)
router.register(r'accounts',AccountViewSet)
router.register(r'transfers' , TransferViewSet)
router.register(r'withrawes' , WithrawViewSet)
router.register(r'deposits' ,DepositViewSet)

urlpatterns = [
    path('bank/',BanksAPIView.as_view() , name = 'banks') ,
    path('branch/' , BranchAPIView.as_view() , name = 'branches') ,
    path('', include(router.urls)) ,
]