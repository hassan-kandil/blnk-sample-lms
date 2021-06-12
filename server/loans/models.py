from django.contrib.auth.models import User
from users.models import Profile
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import numpy as np
from datetime import datetime


class Loan(models.Model):

    Personal = 1
    Mortgage = 2
    Car_Finance = 3
    Travel = 4
    Educational = 5

    LOAN_TYPES = [
        ('personal', 'Personal'),
        ('mortgage', 'Mortgage'),
        ('car finance', 'Car Finance'),
        ('travel', 'Travel'),
        ('educational', 'Educational')
    ]

    monthly = 12
    quarterly = 4
    semi = 2
    annual = 1

    PAYMENTS = [
        (monthly, 'Monthly'),
        (quarterly, 'Quarterly'),
        (semi, 'Semi-Annual'),
        (annual, 'Annual'),
    ]

    id = models.CharField(max_length=100, unique=True, primary_key=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    min_value = models.PositiveIntegerField(blank=True, null=True)
    max_value = models.PositiveIntegerField(blank=True,  null=True)
    duration = models.PositiveIntegerField()
    annual_interest = models.FloatField()
    min_credit_score = models.IntegerField(blank=True, null=True, validators=[
                                           MinValueValidator(400), MaxValueValidator(850)])
    loan_type = models.CharField(
        max_length=20,
        choices=LOAN_TYPES,
        default=Personal
    )
    installment_frequency = models.IntegerField(
        choices=PAYMENTS,
        default=12
    )


class LoanFund(models.Model):

    monthly = 12
    quarterly = 4
    semi = 2
    annual = 1

    PAYMENTS = [
        (monthly, 'Monthly'),
        (quarterly, 'Quarterly'),
        (semi, 'Semi-Annual'),
        (annual, 'Annual'),
    ]


    id = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    min_value = models.PositiveIntegerField(blank=True, null=True)
    max_value = models.PositiveIntegerField(blank=True,  null=True)
    duration = models.PositiveIntegerField()
    annual_interest = models.FloatField()

    installment_frequency = models.IntegerField(
        choices=PAYMENTS,
        default=12
    )


class LoanApplication(models.Model):

    STATUS_VALUES = [
        ('pending', 'Pending Approval'),
        ('missing', 'Missing Documents'),
        ('rejected', 'Rejected'),
        ('approved', 'Approved')
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    amount = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_VALUES,
        default='pending'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                             null=True, related_name='application', related_query_name='application')
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True,
                             null=True, related_name='applications', related_query_name='application')
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='loan', related_query_name='loan')

    installment = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.installment = abs(np.pmt(self.loan.annual_interest/self.loan.installment_frequency,
                                   self.loan.duration*self.loan.installment_frequency, self.amount))
        super(LoanApplication, self).save(*args, **kwargs)


class LoanFundApplication(models.Model):

    STATUS_VALUES = [
        ('pending', 'Pending Approval'),
        ('missing', 'Missing Documents'),
        ('rejected', 'Rejected'),
        ('approved', 'Approved')
    ]

    submitted_by = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    amount = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    installment = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_VALUES,
        default='pending'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                             null=True, related_name='fund_applications', related_query_name='fund_application')
    loanfund = models.ForeignKey(LoanFund, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='applications', related_query_name='application')


    def save(self, *args, **kwargs):
        self.installment = abs(np.pmt(self.loanfund.annual_interest/self.loanfund.installment_frequency,
                                   self.loanfund.duration*self.loanfund.installment_frequency, self.amount))
        super(LoanFundApplication, self).save(*args, **kwargs)


class Amortization(models.Model):

    payment_no = models.PositiveIntegerField(default=0)
    date = models.DateTimeField()
    payment = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    principal = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    interest = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    balance = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)

    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='amortizations', related_query_name='amortization')
    loanfund_application = models.ForeignKey(LoanFundApplication, on_delete=models.CASCADE, blank=True, null=True,
                                             related_name='amortizations', related_query_name='amortization')
