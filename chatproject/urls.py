from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('chat/', views.chat_home, name='chat_home'),
    path('chat/history/<int:user_id>/', views.get_chat_history, name='chat_history'),
]
