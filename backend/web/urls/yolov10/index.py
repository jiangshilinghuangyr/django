from django.urls import path
from web.views.yolov10.yolov10_api import yolov10_api


urlpatterns = [
    path("api/", yolov10_api , name="yolov10_api"),
    # path("playground/", include("web.urls.playground.index")),
    # path("settings/", include("web.urls.settings.index")),
    # path("calculator/", include("web.urls.calculator.index")),
    # path("my_space/", include("web.urls.my_space.index")),
]