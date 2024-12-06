from django.http import JsonResponse
from django.core.paginator import Paginator
from web.models.vermin.vermin import Vermin


def vermin_page_up(request):
    page_number = request.GET.get('page')  # 获取页码，默认为第一页
    page_number = str(int(page_number) - 1)
    verminset = Vermin.objects.all().order_by('-id')
    paginator = Paginator(verminset, 5)  # 每页显示10条数据
    page = paginator.get_page(page_number)  # 获取当前页数据
    data = {
        'message': 'success',
        'vermins': list(page.object_list.values()),  # 将查询集转换为字典列表
        'current_page': page.number,
        'total_pages': paginator.num_pages,
        'total_vermins': paginator.count
    }
    return JsonResponse(data)
