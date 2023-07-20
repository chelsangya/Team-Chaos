from django.urls import path
from metropolition import views 

urlpatterns = [
    path('dashboard/', views.admin, name='admin'),
    path('newnotice/',views.newnotice)
]