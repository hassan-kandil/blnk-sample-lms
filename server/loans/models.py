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

    name = models.CharField(max_length=100, unique=True)
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

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    min_value = models.PositiveIntegerField(blank=True, null=True)
    max_value = models.PositiveIntegerField(blank=True,  null=True)
    duration = models.PositiveIntegerField()
    annual_interest = models.FloatField()
