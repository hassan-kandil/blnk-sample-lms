import django_filters

from .models import *


class LoanFilter(django_filters.FilterSet):
    loan_type = django_filters.ChoiceFilter(choices=Loan.LOAN_TYPES)

    class Meta:
        model = Loan
        fields = '__all__'


class LoanFundFilter(django_filters.FilterSet):

    class Meta:
        model = LoanFund
        fields = '__all__'

class AmortizationFilter(django_filters.FilterSet):
    class Meta:
        model = Amortization
        fields = '__all__'


class LoanApplicationFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=LoanApplication.STATUS_VALUES)
    class Meta:
        model = LoanApplication
        fields = ['id', 'status']