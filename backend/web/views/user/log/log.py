from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth import login
from web.models.user.user import UserDefined


def user_login(request):
    photo_defalut = "https://img0.baidu.com/it/u=4203969099,1267752995&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=667"
    data = request.GET
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
            login(request, user)
            userdefined = UserDefined.objects.get(user=user)
            userdefined.is_online = True
            userdefined.save()
            return JsonResponse({'message': "成功登录",
                                 'photo': photo_defalut,
                                 'id': user.id,
                                 'identity':userdefined.identity,
                                 'sex':userdefined.sex,
                                 'bir': userdefined.birthday,
                                 'email': user.email,
                                 'phone':userdefined.phone_number,
                                 });
    else:
        return JsonResponse({'message': "用户名或密码错误"});


