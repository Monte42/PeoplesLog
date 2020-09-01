from django.urls import path
from . import views
urlpatterns = [
    path('<id>', views.messageView, name='chat'),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
