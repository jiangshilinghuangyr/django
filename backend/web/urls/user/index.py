from django.urls import path
from web.views.user.log.log import user_login
from web.views.user.reg.reg import reg
from web.views.user.set_info.set_info import set_info
from web.views.user.logout.logout import user_logout
from web.views.user.record.get_record import get_record
from web.views.user.record.check_record import check_record
from web.views.user.record.record_pageup import record_pageup
from web.views.user.record.record_pagedown import record_pagedown
from web.views.user.record.delete import delete_record
from web.views.user.post.post_liked import post_liked
from web.views.user.vermin_check.vermin_set import vermin_set
from web.views.user.vermin_check.vermin_pageup import vermin_page_up
from web.views.user.vermin_check.vermin_pagedown import vermin_pagedown
from web.views.user.vermin_check.check_vermin import check_vermin
from web.views.user.dynamic_space.dynamic_space import dynamic_space
from web.views.user.my_space.my_space import my_space
from web.views.user.ai_answer.ai_answer import ai_answer
from web.views.user.post.post_a_post import post_a_post
from web.views.user.ai_answer.check_ai_answer import check_ai_answer
from web.views.user.ai_answer.save import save_ai_answer


urlpatterns = [
    path("log/", user_login, name="user_login"),
    path("reg/", reg, name="reg"),
    path("setinfo/", set_info, name="set_info"),
    path("logout/", user_logout, name="user_logout"),
    path("getrecord/", get_record, name="getRecord"),
    path("checkrecord/", check_record, name="checkrecord"),
    path("recordpageup/", record_pageup, name="recordpageup"),
    path("recordpagedown/", record_pagedown, name="recordpagedown"),
    path("deleterecord/", delete_record, name="deleteRecord"),
    path("verminset/", vermin_set, name="verminset"),
    path("verminpageup/", vermin_page_up, name="verminPageUp"),
    path("verminpagedown/", vermin_pagedown, name="verminPageDown"),
    path("checkvermin/", check_vermin, name="checkVermin"),
    path("dynamicspace/", dynamic_space, name="dynamic_space"),
    path("postliked/", post_liked, name="postliked"),
    path("myspace/", my_space, name="my_space"),
    path("aianswer/", ai_answer, name="ai_answer"),
    path("myspace/", my_space, name="my_space"),
    path("postapost/", post_a_post, name="post_a_post"),
    path("checkaianswer/", check_ai_answer, name="check_ai_answer"),
    path("saveaianswer/", save_ai_answer, name="save_ai_answer"),

    # path("playground/", include("web.urls.playground.index")),
    # path("settings/", include("web.urls.settings.index")),
    # path("calculator/", include("web.urls.calculator.index")),
    # path("my_space/", include("web.urls.my_space.index")),
]
