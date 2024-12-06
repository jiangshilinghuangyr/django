from django.http import JsonResponse
from web.models.record.record import Record


def delete_record(request):
    data = request.POST
    id = data.get('id')
    Record.objects.filter(id=id).delete()
    return JsonResponse({
        'message': 'success',
    })
