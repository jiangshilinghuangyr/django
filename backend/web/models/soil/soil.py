from  django.db import models


class Soil(models.Model):
    """Summary of class here.
    土壤情况表
    """
    soil_type = models.CharField(max_length=100)  #土壤类别
    moisture = models.FloatField(null=True, blank=True)  #湿度

    def __str__(self):
        return str(self.soil_type)
