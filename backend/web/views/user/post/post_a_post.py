from django.http import JsonResponse
from web.models.user.user import UserPost, UserDefined
from datetime import datetime

def post_a_post(request):

    data = request.POST
    user_id = data.get('user_id')
    post_type = data.get('post_type')
    post_content = data.get('post_content')

    user_defined = UserDefined.objects.get(user_id=user_id)
    print(post_type)
    print(post_content)



    UserPost.objects.create(user=user_defined, like=0, content=post_content , post_type=post_type, post_time=datetime.now().replace(microsecond=0))
    return JsonResponse({'message': "success"})
