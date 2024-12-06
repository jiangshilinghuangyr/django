from django.http import JsonResponse
from web.models.vermin.vermin import Vermin


def check_vermin(request):
    data = request.GET
    id = data.get('id')
    vermin = Vermin.objects.get(id=id)
    return JsonResponse({
        'vermin_name' :str(vermin.vermin_name),
        'image_url': str(vermin.image_url),
        'base_info':str(vermin.base_info),
        'suggested_measure':str(vermin.suggested_measure),
    })
