from .models import Loan, LoanFund, LoanApplication
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .filters import *
from .serializers import LoanSerializer, LoanFundSerializer, CreateLoanApplicationSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters



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

        print (self.request.query_params)

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


class LoanApplicationListAPI(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = LoanApplication.objects.all()
    serializer_class = CreateLoanApplicationSerializer
    filterset_class = LoanApplicationFilter
    filter_backends = (filters.DjangoFilterBackend,)




class LoanApplicationAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = LoanApplication.objects.all()
    serializer_class = CreateLoanApplicationSerializer