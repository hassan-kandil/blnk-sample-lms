from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class Address(models.Model):

    apart_no = models.CharField(max_length=5,blank=True, null=True)
    floor_no = models.CharField(max_length=5,blank=True, null=True)
    building_no = models.CharField(max_length=5,blank=True, null=True)
    street =  models.CharField(max_length=255)
    area =  models.CharField(max_length=255)
    city =  models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='address', related_query_name='address')


class Profile(models.Model):
    national_id = models.CharField(max_length=14)
    full_official_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1)
    profession = models.CharField(max_length=255, blank=True, null=True)
    employer = models.CharField(max_length=255, blank=True, null=True)
    monthly_income = models.PositiveIntegerField(blank=True, null=True)
    credit_score = models.IntegerField(blank=True,null=True, validators=[MinValueValidator(400), MaxValueValidator(850)])
    mobile_no = models.CharField(max_length=20)
