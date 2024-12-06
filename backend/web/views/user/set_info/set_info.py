from django.http import JsonResponse
from web.models.user.user import UserDefined


def set_info(request):
    data = request.GET
    userdefined = UserDefined.objects.get(user_id = data['id'])
    username = data.get('username')
    password = data.get('password')
    sex = data.get('sex')
    bir = data.get('bir')
    phone = data.get('phone')
    email = data.get('email')
    userdefined.user.username = username
    userdefined.user.set_password(password)
    userdefined.user.email = email
    userdefined.sex = sex
    userdefined.phone_number = phone
    userdefined.birthday = bir
    userdefined.user.save()
    userdefined.save()
    return JsonResponse({'message': "修改个人信息成功"})