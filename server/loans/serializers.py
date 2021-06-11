from users.serializers import ProfileSerializer, UserSerializer
from django.db import models
from rest_framework import serializers
from .models import Loan, LoanApplication, LoanFund
from users.models import Profile

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


class CreateLoanApplicationSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)
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
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(**profile_data)
        loan_application = LoanApplication.objects.create(profile=profile, user=self._user(),**validated_data)
        return loan_application

        