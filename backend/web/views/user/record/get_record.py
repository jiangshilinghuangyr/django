from django.http import JsonResponse
from web.models.record.record import Record
from web.models.user.user import UserDefined
from django.core.paginator import Paginator


def get_record(request):
    data = request.GET
    id = data.get('id')
    userdefined = UserDefined.objects.get(user_id = id)
    page_number = request.GET.get('page', 1)  # 获取页码，默认为第一页
    records = Record.objects.filter(user=userdefined).order_by('-id')
    paginator = Paginator(records, 7)  # 每页显示10条数据
    page = paginator.get_page(page_number)  # 获取当前页数据
    data = {
        'message': 'success',
        'records': list(page.object_list.values()),  # 将查询集转换为字典列表
        'current_page': page.number,
        'total_pages': paginator.num_pages,
        'total_reports': paginator.count
    }
    return JsonResponse(data)
