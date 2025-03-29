from django.urls import path
from . import views

urlpatterns = [
    # Users
    path('users/get/<str:uid>/', views.get_user, name='get_user'),
    path('users/get-users/', views.get_all_users, name='get_all_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/update/<str:uid>/', views.update_user, name='update_user'),
    path('users/delete/<str:uid>/', views.delete_user, name='delete_user'),

    # Notes
    path('notes/get/<str:note_id>/', views.get_note, name='get_note'),
    path('notes/get-notes/', views.get_all_notes, name='get_all_notes'),
    path('notes/create/', views.create_note, name='create_note'),
    path('notes/update/<str:note_id>/', views.update_note, name='update_note'),
    path('notes/delete/<str:note_id>/', views.delete_note, name='delete_note'),
]
