from django.http import JsonResponse
from django.core.paginator import Paginator
from web.models.user.user import UserPost


def dynamic_space(request):
    page_number = request.GET.get('page', 1)  # 获取页码，默认为第一页
    posts = UserPost.objects.all().order_by("-id")
    usernames = []
    paginator = Paginator(posts, UserPost.objects.count())  # 每页显示10条数据
    page = paginator.get_page(page_number)  # 获取当前页数据
    for post in posts:
        usernames.append(post.user.user.username)
    data = {
        'message': 'success',
        'posts': list(page.object_list.values()),  # 将查询集转换为字典列表
        'current_page': page.number,
        'total_pages': paginator.num_pages,
        'total_posts': paginator.count,
        'usernames': usernames
    }
    print(data)
    return JsonResponse(data)