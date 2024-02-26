from django.urls import path
from . import views

urlpatterns = [
    path('',views.Ourchat, name="Ourchat"),
    path('getroom/',views.getroom, name="getroom"),
    path('send/',views.send, name="send"),
    path('get_messages/<str:room_name>/',views.get_messages, name="get_messages"),
    path('reload/<str:room_name>/<str:username>', views.reload, name="relo")
 ]