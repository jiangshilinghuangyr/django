from django.db import models

#虫害表
class Vermin(models.Model):
    """Summary of class here.
    害虫表   能识别的所有类型
     "0": "asiatic_rice_borer",
     "1": "rice_water_weevil",
     "2": "rice_leaf_roller",
     "3": "rice_gall_midge",
     "4": "brown_plant_hopper",
     "5": "rice_leaf_hopper",
     "6": "small_brown_plant_hopper",
     "7": "yellow_rice_borer",
     "8": "paddy_stem_maggot",
     "9": "rice_leaf_caterpillar"

     "0": "亚洲水稻螟虫",
     "1": "米水象鼻虫",
     “2”：“稻叶卷虫”，
     “3”：“稻瘿蚊”，
     “4”：“棕螟”，
     “5”：“稻叶螟”，
     “6”：“小棕螟”，
     “7”：“黄螟”，
     “8”：“稻茎蛆”，
     “9”：“稻叶毛虫”
    """
    vermin_name = models.CharField(max_length=100)  #害虫名
    base_info = models.TextField(max_length=3000, blank=True, null=True)  #害虫基本信息
    suggested_measure = models.TextField(max_length=3000, blank=True, null=True)  #害虫治理方式
    image_url = models.URLField(max_length=3000, blank=True, null=True)  #害虫图片

    def __str__(self):
        return str(self.vermin_name)



