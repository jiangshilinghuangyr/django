from django.urls import path, include
from web.views.index import index


urlpatterns = [
    path("", index, name="index"),
    path("user/", include("web.urls.user.index")),
    path("yolov10/", include("web.urls.yolov10.index")),
    # path("playground/", include("web.urls.playground.index")),
    # path("settings/", include("web.urls.settings.index")),
    # path("calculator/", include("web.urls.calculator.index")),
    # path("my_space/", include("web.urls.my_space.index")),
]
