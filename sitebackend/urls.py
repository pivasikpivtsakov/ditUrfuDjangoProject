from django.urls import path, include

# api here
from rest_framework import routers

from sitebackend import views
from sitebackend.views import DirectionGroupViewSet

router = routers.DefaultRouter()
router.register('dirgroup', DirectionGroupViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/dirgroupselection/', views.apply_selected_to_db),
]