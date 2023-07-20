from django.urls import path
from citizen import views 

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('safety-and-security/', views.safety, name='safety'),
    path('dashboard/', views.dashboard, name = 'dashboard')

]