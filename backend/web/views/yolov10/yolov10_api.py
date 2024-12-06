import os
import shutil

from django.core.files.storage import FileSystemStorage
from gradio_client import Client, handle_file
from django.http import JsonResponse
from web.models.crop.crop import Crop
from web.models.drone.drone import Drone
from web.models.record.record import Record
from web.models.soil.soil import Soil
from web.models.user.user import UserDefined
from web.models.vermin.vermin import Vermin


def yolov10_api(request):
    fs = FileSystemStorage()

    # 创建 Gradio 客户端，连接到本地运行的 Gradio 应用（地址可以根据实际情况更改）
    client = Client("http://127.0.0.1:7860/")   # 替换为你的 Gradio 应用地址
    video_url = 'https://cdn.acwing.com/static/web/video/video1.mp4'  # 视频文件 URL
    video_file = handle_file(video_url)
    file = request.FILES.get('file')  # 获取名为 'file' 的文件
    filename = fs.save(file.name, file)
    print(filename)
    file_path_final = os.path.join(fs.location, filename)
    result1 = client.predict(
        image = handle_file(file_path_final),
        video = {"video": video_file},  # 提供视频文件和可选的字幕
        model_id = "best.pt",  # 选择使用的模型
        image_size = 640,  # 设置图像处理大小
        conf_threshold = 0.25,  # 设置置信度阈值
        input_type = "Image",  # 输入类型，这里选择图像（'Image' 或 'Video'）
        api_name = "/run_inference"  # 调用的 API 名称
    )
    id = request.POST.get('id')
    userdefined = UserDefined.objects.get(user_id=id)
    vermin_list = Vermin.objects.filter(vermin_name=result1[1])
    if vermin_list.exists():
        vermin = vermin_list[0]
    else:
        return JsonResponse({'message': "未成功识别",
                             'path': filename,
                             'type': "无",
                             })
    source_path = result1[0]
    destination_path = "C:/Users/jiang/Desktop/pyCharm/daoolun/backend/web/media/image/"
    records = Record.objects.filter(user=userdefined)
    if records :
        file_name = str(id)+"image" + str(Record.objects.filter(user__user_id=id).count()+1) + ".webp"
    else:
        file_name = str(id)+"image" + "1" + ".webp"
    destination_path = os.path.join(destination_path, file_name)
    shutil.copy(source_path, destination_path)
    drone = Drone.objects.filter(owner=userdefined).first()
    crop  = Crop.objects.get(crop_name="水稻")
    soil = Soil.objects.get(soil_type="中性土")
    weather = "长沙阴雨绵绵"
    Record.objects.create(user=userdefined, drone =drone, vermin=vermin, crop=crop, soil=soil
                          , weather=weather, temperature=14.3, photo=file_name, photo_record_method=1)
    return JsonResponse({'message': "成功识别",
                         'path':file_name ,
                         'type': result1[1],
                         })




