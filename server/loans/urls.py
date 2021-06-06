from django.db import router
from rest_framework import routers
from .api import LoanViewSet, LoanFundViewSet

router = routers.DefaultRouter()
router.register('api/loans', LoanViewSet, 'loans')
router.register('api/loanfunds', LoanFundViewSet, 'loanfunds')

urlpatterns = router.urls