from django.urls import path
from blog.views import create, list, update, delete

urlpatterns = [
    path('create/', create, name='create'),
    path('list/', list, name='list'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
]