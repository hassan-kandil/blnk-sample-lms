from .models import Loan, LoanFund, LoanApplication, Amortization, LoanFundApplication
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .filters import *
from .serializers import *
from rest_framework.response import Response
from django_filters import rest_framework as filters
from users.models import User
from users.permission import IsAdminUser, IsLoggedInUserOrAdmin, IsAdminOrAnonymousUser


# Loan Viewset
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    persmissions_classes = [IsAuthenticated]
    filterset_class = LoanFilter
    serializer_class = LoanSerializer

    # def get_queryset(self):
    #     print (self.request.query_params)
    #     if (self.request.query_params.get('fields[loans][0]') == 'id'):
    #         print('hereee')
    #         loan_ids = Loan.objects.values_list('id', flat=True)
    #         return loan_ids

    #     return Loan.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if (self.request.query_params.get('fields[loans][1]') == 'label'):
            print('hereee')
            loan_ids = Loan.objects.values_list('id', flat=True)
            return Response(list(loan_ids))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# LoanFund Viewset
class LoanFundViewSet(viewsets.ModelViewSet):
    queryset = LoanFund.objects.all()
    persmissions_classes = [IsAuthenticated]
    serializer_class = LoanFundSerializer
    filterset_class = LoanFundFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if (self.request.query_params.get('fields[loan-funds][1]') == 'label'):
            loanfund_ids = LoanFund.objects.values_list('id', flat=True)
            return Response(list(loanfund_ids))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AmortizationViewSet(viewsets.ModelViewSet):
    queryset = Amortization.objects.all().order_by('id')
    persmissions_classes = [IsAuthenticated]
    serializer_class = AmortizationSerializer
    filterset_class = AmortizationFilter

class LoanApplicationListAPI(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = LoanApplication.objects.all().order_by('id')
    serializer_class = CreateLoanApplicationSerializer
    filterset_class = LoanApplicationFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        user = User.objects.get(username=self.request.user)

        if not user.groups.filter(name="admin"):
            queryset = queryset.filter(user=user.id)

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def create(self, request):
    #     serializer = CreateLoanApplicationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': 'issue created'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanFundApplicationListAPI(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = LoanFundApplication.objects.all().order_by('id')
    serializer_class = CreateLoanFundApplicationSerializer
    filterset_class = LoanFundApplicationFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        user = User.objects.get(username=self.request.user)

        if not user.groups.filter(name="admin"):
            queryset = queryset.filter(user=user.id)

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class LoanApplicationAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = LoanApplication.objects.all()
    serializer_class = UpdateLoanApplicationSerializer

class LoanFundApplicationAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = LoanFundApplication.objects.all()
    serializer_class = UpdateLoanFundApplicationSerializer


# class LoanApplicationAPI(generics.RetrieveDestroyAPIView):
#     permission_classes = [
#         IsAuthenticated,
#     ]
#     queryset = LoanApplication.objects.all()
#     serializer_class = GetLoanApplicationSerializer