from rest_framework import routers
from django.urls import path,include

from . import views #from current directory

router = routers.DefaultRouter()
router.register(r'', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]