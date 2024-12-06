from django.http import JsonResponse
from web.models.crop.crop import Crop
from web.models.drone.drone import Drone
from web.models.record.record import Record
from web.models.soil.soil import Soil
from web.models.vermin.vermin import Vermin


def check_record(request):
    data = request.GET
    id = data.get('id')
    record = Record.objects.get(id=id)
    crop_id = record.crop_id
    crop = Crop.objects.get(id=crop_id)
    vermin_id = record.vermin_id
    vermin = Vermin.objects.get(id=vermin_id)
    soil_id = record.soil_id
    soil = Soil.objects.get(id=soil_id)
    drone_id = record.drone_id
    drone = Drone.objects.get(id=drone_id)
    return JsonResponse({
        'photo' :str(record.photo),
    'date': str(record.gen_date),
    'weather' :str(record.weather),
    'temperature' :str(record.temperature),
    'crop_name' :str(crop.crop_name),
    'crop_basic' :str(crop.base_info),
    'crop_habit' :str(crop.growth_habit),
    'vermin_name': str(vermin.vermin_name),
    'vermin_basic': str(vermin.base_info),
    'vermin_measure': str(vermin.suggested_measure),
    'soil_name': str(soil.soil_type),
    'soil_moisture': str(soil.moisture),
    'drone_name' :str(drone.drone_name),
    'drone_pro' :str(drone.manufacturer),
    'drone_date' :str(drone.pro_date),
    })
