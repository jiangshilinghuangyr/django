from datetime import date
from django.db import models
from web.models.user.user import UserDefined


class Drone(models.Model):
    """Summary of class here.
       无人机表
       """
    owner = models.ForeignKey(UserDefined, on_delete=models.CASCADE)  #拥有者
    drone_name = models.CharField(max_length=100, null=True, blank=True, default='无人机1号')  #给无人机取的名字
    pro_date = models.DateField(default=date.today, null=True, blank=True)  #无人机生产日期
    is_delete = models.BooleanField(default=False, null=True, blank=True)  #是否删除
    manufacturer = models.CharField(max_length=100, null=True, blank=True)  #厂商信息

    def __str__(self):
        return str(self.owner.user.username+" "+" "+self.manufacturer+":"+self.drone_name)