from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Donor(models.Model):
    donorID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, validators=[
        MinValueValidator(2, "The first name must be longer than 2 characters")
    ])
    lastName = models.CharField(max_length=50, null=False)
    bloodVariety = models.CharField(max_length=10, null=False)
    address = models.TextField(max_length=100, validators=[
        MinValueValidator(2, "Address must be longer than 2 characters")])
    email = models.EmailField(max_length=20)
    phoneNumber = models.IntegerField(max_length=15, null=False)
    DOB = models.DateField()

    object = models.manager

    def __str__(self):
        return self.firstName + self.lastName


class Worker(models.Model):
    workerID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, validators=[
        MinValueValidator(2, "The first name must be longer than 2 characters")
    ])
    lastName = models.CharField(max_length=50, null=False)
    address = models.TextField(max_length=100, validators=[
        MinValueValidator(2, "Address must be longer than 2 characters")])
    email = models.EmailField(max_length=20)
    phoneNumber = models.IntegerField(max_length=15, null=False)

    object = models.manager

    def __str__(self):
        return self.firstName + self.lastName


class CampDetails(models.Model):
    campID = models.AutoField(primary_key=True)
    address = models.TextField(max_length=100, validators=[
        MinValueValidator(2, "Address must be longer than 2 characters")])
    OrgName = models.CharField(max_length=50, validators=[
        MinValueValidator(2, "Organisation name must be longer than 2 characters")])

    object = models.manager

    def __str__(self):
        return self.OrgName


class DonationCamp(models.Model):
    donationID = models.AutoField(primary_key=True)
    donorID = models.ForeignKey(Donor,on_delete=models.CASCADE)
    workerID = models.ForeignKey(Worker,on_delete=models.CASCADE)
    campID = models.ForeignKey(CampDetails,on_delete=models.CASCADE)

    object = models.manager

    def __str__(self):
        return self.donationID

