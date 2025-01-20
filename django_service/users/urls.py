from django.urls import path
from . import views

# urlpatterns = [
#     path('users/', views.user_list, name='user_list'),
#     path('users/<int:user_id>/', views.user_detail, name='user_detail'),
#     path('users/create/', views.user_create, name='user_create'),
#     path('users/update/<int:user_id>/', views.user_update, name='user_update'),
#     path('users/delete/<int:user_id>/', views.user_delete, name='user_delete'),
# ]
# urlpatterns = [
#     path('', views.user_list_view, name='user_list'),
#     path('<int:user_id>/', views.user_detail_view, name='user_detail'),
#     path('create/', views.user_create_view, name='user_create'),
#     path('update/<int:user_id>/', views.user_update_view, name='user_update'),  # Route pour update
#     path('delete/<int:user_id>/', views.user_delete_view, name='user_delete'),  # Route pour delete
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list_view, name='user_list'),
    path('create/', views.user_create_view, name='user_create'),
    path('update/<int:user_id>/', views.user_update_view, name='user_update'),
    path('delete/<int:user_id>/', views.user_delete_view, name='user_delete'),
]