from django.http import JsonResponse
from web.models.user.user import  UserPost


def post_liked(request):
    data = request.POST
    id = data.get('post_id')
    post = UserPost.objects.get(id=id)
    post.like = post.like+1
    post.save()
    return JsonResponse({'message': "成功点赞"})
