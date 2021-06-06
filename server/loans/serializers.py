from django.db import models
from rest_framework import serializers
from .models import Loan, LoanFund

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


class LoanFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFund
        fields = '__all__'