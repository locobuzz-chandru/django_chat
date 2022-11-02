from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_group, name='add'),
    path('delete/<int:id>/', views.delete_group, name='delete'),
    path('edit/<int:id>/', views.edit_group, name='edit'),
    path('update/<int:id>/', views.update_group, name='update'),
    path('members/<int:group_id>/', views.get_members, name='members'),
    path('add_member/<int:group_id>/<int:user_id>/', views.add_member, name='add_member'),
    path('remove_member/<int:group_id>/<int:user_id>/', views.remove_member, name='remove_member'),
    path('room/<str:room_name>/', views.chat_room_view, name='chatroom')
]
