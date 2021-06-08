from .models import Loan, LoanFund
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .filters import LoanFilter
from .serializers import LoanSerializer, LoanFundSerializer

# Loan Viewset
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    persmissions_classes = [AllowAny]
    filterset_class = LoanFilter
    serializer_class = LoanSerializer


# LoanFund Viewset
class LoanFundViewSet(viewsets.ModelViewSet):
    queryset = LoanFund.objects.all()
    persmissions_classes = [AllowAny]
    serializer_class = LoanFundSerializer