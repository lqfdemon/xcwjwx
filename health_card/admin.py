from django.contrib import admin
from health_card.models import HealthCardInfo,SalaryBankInfo,EducationInfo,NationInfo

admin.site.register(HealthCardInfo)
admin.site.register(SalaryBankInfo)
admin.site.register(EducationInfo)
admin.site.register(NationInfo)
# Register your models here.
