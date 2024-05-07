from django.urls import path
from blog.views import create, list, detail, update, delete

urlpatterns = [
    path('create/', create, name='create'),
    path('list/', list, name='list'),
    path('detail/', detail, name='detail'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
]