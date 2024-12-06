from django.http import JsonResponse
from django.contrib.auth import logout
from web.models.user.user import UserDefined


def user_logout(request):
    data = request.GET
    id = data.get('id')
    userdefined = UserDefined.objects.get(user_id = id)
    userdefined.is_online = False
    userdefined.save()
    logout(request)
    return JsonResponse({'message': "成功退出"})
