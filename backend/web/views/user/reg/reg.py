from django.contrib.auth import login
from django.http import JsonResponse
from web.models.drone.drone import Drone
from web.models.user.user import UserDefined
from django.contrib.auth.models import User


def reg(request):
    data = request.GET
    username = data.get('username')
    password = data.get('password')
    password_conf = data.get('passwordConf')
    if User.objects.filter(username=username).exists():
        return JsonResponse({'message': "用户名已存在"})
    if password_conf != password:
        return JsonResponse({'message': "两次密码不一致"})
    user = User(username=username)
    user.set_password(password)
    user.save()
    login(request, user)
    userdefined = UserDefined(user=user)
    userdefined.is_online = True
    photo_defalut = "https://img0.baidu.com/it/u=4203969099,1267752995&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=667"
    userdefined.photo = photo_defalut
    userdefined.save()
    Drone.objects.create(owner=userdefined, drone_name="无人机1号", manufacturer="大疆test系列")
    return JsonResponse({'message': "成功注册",
                         'photo':photo_defalut,
                         'id': user.id,
                         })






