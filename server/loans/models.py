from django.contrib.auth.models import User
from users.models import Profile
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


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

    id = models.CharField(max_length=100, unique=True, primary_key=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    min_value = models.PositiveIntegerField(blank=True, null=True)
    max_value = models.PositiveIntegerField(blank=True,  null=True)
    duration = models.PositiveIntegerField()
    annual_interest = models.FloatField()
    min_credit_score = models.IntegerField(blank=True,null=True, validators=[MinValueValidator(400), MaxValueValidator(850)])
    loan_type = models.CharField(
        max_length=20,
        choices=LOAN_TYPES,
        default=Personal
    )

class LoanFund(models.Model):

    id = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    min_value = models.PositiveIntegerField(blank=True, null=True)
    max_value = models.PositiveIntegerField(blank=True,  null=True)
    duration = models.PositiveIntegerField()
    annual_interest = models.FloatField()


class LoanApplication(models.Model):

    STATUS_VALUES = [
        ('pending', 'Pending Approval'),
        ('missing', 'Missing Documents'),
        ('rejected', 'Rejected'),
        ('approved', 'Approved')
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_VALUES,
        default='pending'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='application', related_query_name='application')
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True, related_name='applications', related_query_name='application')
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name='loan', related_query_name='loan')