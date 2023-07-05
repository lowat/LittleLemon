from django.contrib import admin 
from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('menuitem/', views.MenuItemView.as_view()),
    path('menuitem/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]