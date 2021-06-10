from django.db import router
from rest_framework import routers
from .api import LoanViewSet, LoanFundViewSet

from rest_framework.routers import DefaultRouter


class CustomDefaultRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = '/?'

router = CustomDefaultRouter()
router.register('api/loans', LoanViewSet, 'loans')
router.register('api/loan-funds', LoanFundViewSet, 'loan-funds')

urlpatterns = router.urls