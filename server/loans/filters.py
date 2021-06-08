import django_filters

from .models import Loan


class LoanFilter(django_filters.FilterSet):
    loan_type = django_filters.ChoiceFilter(choices=Loan.LOAN_TYPES)

    class Meta:
        model = Loan
        fields = '__all__'

