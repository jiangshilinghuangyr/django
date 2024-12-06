from django.http import JsonResponse
from django.core.paginator import Paginator
from web.models.user.user import UserQuesSaved, UserDefined


def check_ai_answer(request):
    data = request.GET
    userid = data.get('userid')
    page_number = request.GET.get('page', 1)  # 获取页码，默认为第一页
    userdefined = UserDefined.objects.get(user_id=userid)
    ai_answer = UserQuesSaved.objects.filter(user_id=userdefined.id).order_by('-id')
    paginator = Paginator(ai_answer, ai_answer.count())  # 每页显示10条数据
    page = paginator.get_page(page_number)  # 获取当前页数据
    data = {
        'message': 'success',
        'ai_answers': list(page.object_list.values()),  # 将查询集转换为字典列表
        'current_page': page.number,
        'total_pages': paginator.num_pages,
        'total_ai_answers': paginator.count
    }
    print(data)
    return JsonResponse(data)