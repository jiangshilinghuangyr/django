from django.db import models


class Crop(models.Model):
    """Summary of class here.
    作物表
    """
    crop_name = models.CharField(max_length=100)  #名
    base_info = models.TextField(max_length=3000, blank=True, null=True)  #基本信息
    growth_habit = models.TextField(max_length=3000, blank=True, null=True)  #生长喜好

    def __str__(self):
        return str(self.crop_name)