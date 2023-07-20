from django.urls import path


from citizen.views import submit_report

urlpatterns = [
    path('report', submit_report, name='report'),
]