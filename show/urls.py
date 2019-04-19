from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/department/', views.get_department),
    url(r'^api/story/', views.get_story),
    url(r'^api/member_list/', views.get_member_list),
    url(r'^api/member/', views.get_member_of_the_year),
    url(r'^api/work/', views.get_work),
    url(r'^api/comment_list/', views.get_comment_list),
    url(r'^api/comment/', views.comment),
]

