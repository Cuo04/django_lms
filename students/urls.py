from django.urls import path
from . import views


app_name = 'students'
urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.register_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_request, name='logout')
]
