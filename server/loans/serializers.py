from users.serializers import ProfileSerializer, UserSerializer
from django.db import models
from rest_framework import serializers
from .models import Loan, LoanApplication, LoanFund, Amortization
from users.models import Profile
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
import numpy as np


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
    annual_interest = PercentageField()
    class Meta:
        model = LoanFund
        fields = '__all__'

class AmortizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amortization
        fields = '__all__'


class CreateLoanApplicationSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()
    loan = LoanSerializer(read_only=True)
    loan_id = serializers.PrimaryKeyRelatedField(queryset=Loan.objects.all(), source='loan')
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = LoanApplication
        fields = '__all__'

    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.user

    def create(self, validated_data):
        print (validated_data)
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(**profile_data)
        loan_application = LoanApplication.objects.create(profile=profile, user=self._user(),**validated_data)


        ending_balance= loan_application.amount
        for per in range(1,(loan_application.loan.duration*loan_application.loan.installment_frequency)+1):
            date = loan_application.start_date + relativedelta(months=+int(12/loan_application.loan.installment_frequency*per))
            # Calculate the interest
            interest = abs(np.ipmt(loan_application.loan.annual_interest/loan_application.loan.installment_frequency, per, 
                                   loan_application.loan.duration*loan_application.loan.installment_frequency, loan_application.amount))

            # Calculate the principal
            principal = abs(np.ppmt(loan_application.loan.annual_interest/loan_application.loan.installment_frequency, per, 
                                   loan_application.loan.duration*loan_application.loan.installment_frequency, loan_application.amount))
            
            print('Per ', per)
            print('Date ', date)
            print('Balance ', ending_balance)
            print('Interest ', interest)
            print('Principal ', principal)

            ending_balance = ending_balance - principal

            amortization = Amortization.objects.create(loan_application=loan_application, payment_no=per, date=date, interest=interest, principal=principal, balance=ending_balance)



        return loan_application


class UpdateLoanApplicationSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()
    loan_id = serializers.PrimaryKeyRelatedField(queryset=Loan.objects.all(), source='loan')
    loan = LoanSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    amortizations = AmortizationSerializer(read_only=True, many=True)



    class Meta:
        model = LoanApplication
        fields = ('amount', 'loan_id', 'notes', 'status', 'profile', 'user', 'amortizations', 'loan')


    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.loan_id = validated_data.get('loan_id', instance.loan_id)
        instance.notes = validated_data.get( 'notes', instance.notes)
        instance.status = validated_data.get('status', instance.status)
        profile_data = validated_data.get('profile')

        if(profile_data):
            profile, created = Profile.objects.get_or_create(loan=instance, **profile_data)
            if not created:
                instance.profile = profile

        instance.save()
        return instance

# class GetLoanApplicationSerializer(serializers.ModelSerializer):

#     profile = ProfileSerializer()
#     loan = LoanSerializer(read_only=True)
#     loan_id = serializers.PrimaryKeyRelatedField(queryset=Loan.objects.all(), source='loan')
#     user = UserSerializer(read_only=True)
#     amortizations = AmortizationSerializer(read_only=True, many=True)
    
#     class Meta:
#         model = LoanApplication
#         fields = '__all__'
