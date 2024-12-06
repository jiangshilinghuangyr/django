from django.contrib import admin
from web.models.user.user import UserDefined
from web.models.user.user import UserPost
from web.models.vermin.vermin import Vermin
from web.models.crop.crop import Crop
from web.models.soil.soil import Soil
from web.models.drone.drone import Drone
from web.models.record.record import Record
from web.models.user.user import UserQuesSaved


class UserQuesSavedAdmin(admin.ModelAdmin):
    """Summary of class here.
    管理admin对UserQuesSaved表的权限
    """
    list_display = ('user', 'ques', 'ai_answer')

    def get_status_count(self, obj):
        return UserQuesSaved.objects.filter(active=obj.active).count()

    get_status_count.short_description = 'Active Status Count'

class UserDefinedAdmin(admin.ModelAdmin):
    """Summary of class here.
    管理admin对UserDefined表的权限
    """
    list_display = ('user', 'sex', 'birthday', 'current_drone', 'drone_total', 'identity', 'is_online', 'phone_number')
    ordering = ['birthday']
    list_filter = ('sex', 'is_online', 'identity')
    search_fields = ['user__username', 'phone_number']

    def get_status_count(self, obj):
        return UserDefined.objects.filter(active=obj.active).count()

    get_status_count.short_description = 'Active Status Count'

class DronedAdmin(admin.ModelAdmin):
    """Summary of class here.
    管理admin对Drone表的权限
    """
    list_display = ('owner', 'pro_date', 'manufacturer')
    ordering = ['pro_date']
    list_filter = ('owner', 'manufacturer')
    search_fields = ['owner__user__username']

    def get_status_count(self, obj):
        return Drone.objects.filter(active=obj.active).count()

    get_status_count.short_description = 'Active Status Count'


class RecordAdmin(admin.ModelAdmin):
    """Summary of class here.
    管理admin对Record表的权限
    """
    list_display = ('user', 'drone', 'vermin', 'crop', 'soil' , 'gen_date', 'id')
    ordering = ['gen_date']
    list_filter = ('user', 'vermin', 'crop', 'soil')
    search_fields = ['user__user__username', 'drone__drone_name', 'vermin__vermin_name', 'soil__soil_type', 'crop__crop_name']

    def get_status_count(self, obj):
        return Record.objects.filter(active=obj.active).count()

    get_status_count.short_description = 'Active Status Count'


# Register your models here.
admin.site.register(UserDefined,UserDefinedAdmin)
admin.site.register(UserPost)
admin.site.register(Vermin)
admin.site.register(Crop)
admin.site.register(Soil)
admin.site.register(Drone,DronedAdmin)
admin.site.register(Record,RecordAdmin)
admin.site.register(UserQuesSaved,UserQuesSavedAdmin)

