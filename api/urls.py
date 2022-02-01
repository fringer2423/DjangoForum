from django.urls import path, include
from rest_framework import routers
# from .views import CheckboxViewset
from .views import *

# router = routers.DefaultRouter()
# router.register('checkbox', CheckboxViewset)

urlpatterns = [
    # path('', include(router.urls)),
    path('checkbox_list', checkbox_list, name='checkbox_list'),
    path('checkbox_list/<int:pk>', checkbox_detail, name='checkbox_detail'),
    path('checkbox_create', checkbox_create, name='checkbox_create'),
    path('checkbox_update/<int:pk>', checkbox_update, name='checkbox_update'),
    path('checkbox_delete/<int:pk>', checkbox_delete, name='checkbox_delete'),
]
