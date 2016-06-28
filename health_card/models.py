#-*-coding:UTF-8-*-
from django.db import models

class BankInfo(models.Model):
    bank_name = models.CharField(max_length=20,unique=True)

    def __unicode__(self):
        return self.bank_name

class NationInfo(models.Model):
    nation = models.CharField(max_length=10,unique=True)

    def __unicode__(self):
        return self.nation

class EducationInfo(models.Model):
    education_back = models.CharField(max_length=30,unique=True)

    def __unicode__(self):
        return self.education_back

class HealthCardInfo(models.Model):
    name = models.CharField(max_length=20,unique=True)
    bank_name =models.ForeignKey(BankInfo,null=True)
    nation = models.ForeignKey(NationInfo,null=True)
    education_back =models.ForeignKey(EducationInfo,null=True)

    def __unicode__(self):
        return self.name

# Create your models here.
