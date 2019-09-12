from django.db import models


class Customer(models.Model):

    customer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name


# model for Edc mapping
class EDCModel(models.Model):

    code = models.CharField(max_length=3)
    place = models.CharField(max_length=25)

    def __str__(self):

        return self.code


# Model for customer mapping

class ServiceGroup(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    serviceNumber = models.CharField(max_length=12, unique=True)
    edc = models.ForeignKey(EDCModel, on_delete=models.CASCADE)

    def __str__(self):

        return self.serviceNumber


class Readings(models.Model):

    consumerID = models.CharField(max_length=12)
    statementMonth = models.CharField(max_length=2)
    statementYear = models.CharField(max_length=4)
    impUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2)
    impUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2)
    impUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2)
    impUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2)
    impUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2)
    expUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2)
    expUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2)
    expUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2)
    expUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2)
    expUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2)
    netUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2)
    netUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2)
    netUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2)
    netUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2)
    netUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2)
    bankingC1 = models.DecimalField(max_digits=12, decimal_places=2)
    bankingC2 = models.DecimalField(max_digits=12, decimal_places=2)
    bankingC3 = models.DecimalField(max_digits=12, decimal_places=2)
    bankingC4 = models.DecimalField(max_digits=12, decimal_places=2)
    bankingC5 = models.DecimalField(max_digits=12, decimal_places=2)
    chargesC002 = models.DecimalField(max_digits=12, decimal_places=2)
    chargesC003 = models.DecimalField(max_digits=12, decimal_places=2)
    chargesC004 = models.DecimalField(max_digits=12, decimal_places=2)
    chargesC005 = models.DecimalField(max_digits=12, decimal_places=2)
    chargesC006 = models.DecimalField(max_digits=12, decimal_places=2)
    chargesC007 = models.DecimalField(max_digits=12, decimal_places=2)
    chargesC001 = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):

        return self.consumerID + '_' + self.statementMonth + self.statementYear
