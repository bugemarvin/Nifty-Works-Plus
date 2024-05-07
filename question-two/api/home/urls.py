from django.urls import path
from home.views import Homeview

urlpatterns = [
        path('api/v1/', Homeview, name='home'),
]