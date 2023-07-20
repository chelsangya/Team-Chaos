from django.urls import path
from .views import login,register,safety,dashboard,submit_report

urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('safety-and-security/', safety, name='safety'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('report/',submit_report)
    

]