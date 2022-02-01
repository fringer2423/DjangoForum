from django.urls import path, include
from rest_framework import routers
from .views import CheckboxViewset

router = routers.DefaultRouter()
router.register('checkbox', CheckboxViewset)

urlpatterns = [
    path('', include(router.urls)),
]
