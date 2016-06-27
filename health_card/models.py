from django.db import models

class HealthCardInfo(models.Model):
    name = models.CharField(max_length=20,unique=True)

    def __unicode__(self):
        return self.name
# Create your models here.
