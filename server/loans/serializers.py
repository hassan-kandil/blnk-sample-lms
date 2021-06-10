from django.db import models
from rest_framework import serializers
from .models import Loan, LoanFund

# class ChoiceField(serializers.ChoiceField):

    # def to_representation(self, obj):
    #     if obj == '' and self.allow_blank:
    #         return obj
    #     return self._choices[obj]

    # def to_internal_value(self, data):
    #     # To support inserts with the value
    #     if data == '' and self.allow_blank:
    #         return ''

    #     for key, val in self._choices.items():
    #         if val == data:
    #             return key
    #     self.fail('invalid_choice', input=data)


class PercentageField(serializers.Field):

    def to_representation(self, data):
        return data

    def to_internal_value(self, data):
        return float(data) / 100.0
class LoanSerializer(serializers.ModelSerializer):

    annual_interest = PercentageField()
    class Meta:
        model = Loan
        fields = '__all__'

    # loan_type = ChoiceField(choices=Loan.LOAN_TYPES)



class LoanFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFund
        fields = '__all__'