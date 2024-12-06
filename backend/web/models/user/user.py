from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import User


class UserDefined(models.Model):
    """Summary of class here.
    自定义用户表 继承自Django自带的用户表
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #和Django自带的用户系统绑定
    sex = models.CharField(max_length=10, null=True, blank=True)  #性别
    photo = models.URLField(max_length=3000, null=True, blank=True)  #头像
    birthday = models.DateField(default=date.today, null=True, blank=True)  #生日
    current_drone = models.IntegerField(null=True, blank=True)  #正在使用的无人机
    drone_total = models.IntegerField(default=1, null=True, blank=True)  #该用户的无人机总数
    identity = models.IntegerField(default=0, null=True, blank=True)  #身份
    is_online = models.BooleanField(default=False, null=True, blank=True)  #是否在线
    phone_number = models.CharField(max_length=100, null=True, blank=True)  #电话号码

    def __str__(self):
        return str(self.user)


class UserPost(models.Model):
    """Summary of class here.
    用户帖子表
    """
    user = models.ForeignKey(UserDefined, on_delete=models.CASCADE, null=True, blank=True)  #和自定义用户绑定
    like = models.IntegerField(default=0, null=True, blank=True)  #点赞数
    content = models.TextField(max_length=10000, null=True, blank=True)  #帖子文本内容
    post_date = models.DateField(default=date.today, null=True, blank=True)  #帖子年月日
    post_type = models.CharField(max_length=100, null=True, blank=True)  #帖子类型
    post_time = models.TimeField(default=datetime.now, null=True, blank=True)  #帖子时分秒

    def __str__(self):
        return str(self.user)




class UserQuesSaved(models.Model):
    """Summary of class here.
    用户提问保留表
    """
    user = models.ForeignKey(UserDefined, on_delete=models.CASCADE, null=True, blank=True)  #和自定义用户绑定
    ques = models.TextField(max_length=10000, null=True, blank=True)
    ai_answer = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return str(self.user)




