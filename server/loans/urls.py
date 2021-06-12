from django.db import router
from django.urls import path, include

from rest_framework import routers
from .api import LoanApplicationListAPI, LoanViewSet, LoanFundViewSet, LoanApplicationAPI, AmortizationViewSet, LoanFundApplicationAPI, LoanFundApplicationListAPI, ProfitListAPI, TotalStatsAPI

from rest_framework.routers import DefaultRouter


class CustomDefaultRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = '/?'

router = CustomDefaultRouter()
router.register('api/loans', LoanViewSet, 'loans')
router.register('api/loan-funds', LoanFundViewSet, 'loan-funds')
router.register('api/amortizations', AmortizationViewSet, 'amortizations')


urlpatterns = [
    path('api/loan-applications', LoanApplicationListAPI.as_view()),
    path('api/loan-applications/<int:pk>', LoanApplicationAPI.as_view()),
    path('api/loan-fund-applications', LoanFundApplicationListAPI.as_view()),
    path('api/loan-fund-applications/<int:pk>', LoanFundApplicationAPI.as_view()),
    path('api/profit-stats', ProfitListAPI.as_view()),
    path('api/total-stats', TotalStatsAPI.as_view()),

    path('', include(router.urls))
]