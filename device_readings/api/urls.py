from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import latest_device, manage_devices, manage_device, sum_device

urlpatterns = {
    path('devices', manage_devices, name="devices"),
    path('devices/<slug:id>', manage_device, name="device"),
    path('devices/<slug:id>/sum', sum_device, name="device_sum"),
    path('devices/<slug:id>/latest', latest_device, name="device_latest")
}

urlpatterns = format_suffix_patterns(urlpatterns)
