from django.urls import path, re_path
from django.conf.urls import url, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('',views.PostViewSet)

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/',include(router.urls)),
    re_path(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    # path('api/list/', views.PostListView.as_view(), name='api'),
    # path('api/<pk>', views.PostDetailView.as_view(), name='detail'),
]
