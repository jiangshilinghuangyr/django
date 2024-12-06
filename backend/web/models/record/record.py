from datetime import date
from django.db import models
from web.models.crop.crop import Crop
from web.models.drone.drone import Drone
from web.models.soil.soil import Soil
from web.models.user.user import UserDefined
from web.models.vermin.vermin import Vermin


class Record(models.Model):
    """Summary of class here.
       报告记录表
       """
    gen_date = models.DateField(default=date.today)  #报告生成日期
    user = models.ForeignKey(UserDefined, on_delete=models.CASCADE)  #谁生成了报告
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)  #报告使用了哪台无人机
    vermin = models.ForeignKey(Vermin, on_delete=models.CASCADE)  #此次报告中出现的害虫信息
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)  #此次报告中出现的作物信息
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE)  #此次报告中出现的土壤信息
    weather = models.TextField(max_length=100, null=True, blank=True)  #此次报告中出现的天气信息
    temperature = models.FloatField(null=True, blank=True)  #此次报告中出现的气温信息
    photo = models.URLField(max_length=3000, null=True, blank=True)  #识别过的图片的公开url地址
    photo_record_method = models.IntegerField(null=True, blank=True)  #0机飞 1人飞 摆设

    def __str__(self):
        return str(self.user.user.username+" 生成日期"+str(self.gen_date)+" "+self.drone.manufacturer+":"+self.drone.drone_name)
