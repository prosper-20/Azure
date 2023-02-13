from django.urls import path
from .views import api_post_list, api_post_detail, Api_post_list, Api_post_detail

urlpatterns = [
    path("home/", api_post_list, name="post_list"),
    path("home2", Api_post_list.as_view(), name="Api-post-list"),
    path("<int:pk>/", api_post_detail, name="post-detail"),
    path("<int:pk>/detail", Api_post_detail.as_view(), name="post-detail-2")
    
]