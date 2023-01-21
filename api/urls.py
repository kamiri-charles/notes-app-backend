from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='api'),

    # Notes
    path('notes/<str:username>/', views.notes, name='get_notes'),
    path('note/<str:pk>/', views.note_detail, name='note_detail'),
    path('notes/new/', views.note_create, name='note_create'),
    path('notes/update/<str:pk>/', views.note_update, name='note_update'),
    path('notes/delete/<str:pk>/', views.note_delete, name='note_delete'),

    # Users
    path('user/', views.user, name='user_info'),
    path('user/sign-up/', views.user_create, name='user_create'),
    path('user/sign-in/', views.user_sign_in, name='user_sign_in'),
    path('user/sign-out/', views.user_sign_out, name='user_sign_out'),
    path('user/update/<str:username>/', views.user_update, name='user_update'),
    path('user/delete/<str:username>/', views.user_delete, name='user_delete'),
]