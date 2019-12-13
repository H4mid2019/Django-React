from blog.views import PostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('blog',PostViewSet)