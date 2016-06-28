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

class UnitInfo(models.Model):
    unit_name = models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return self.unit_name

class HealthCardInfo(models.Model):
    name = models.CharField(max_length=20,unique=True)
    id_num = models.IntegerField(unique=True,default=0)
    bank_name =models.ForeignKey(BankInfo,null=True)
    nation = models.ForeignKey(NationInfo,null=True)
    education_back =models.ForeignKey(EducationInfo,null=True)
    unit_name=models.ForeignKey(UnitInfo,null=True)
    book_address=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    tel=models.IntegerField(unique=True,default=0)
    nonghe_id=models.IntegerField(unique=True,default=0)
    shebao_id=models.IntegerField(unique=True,default=0)
    def __unicode__(self):
        return self.name

# Create your models here.
