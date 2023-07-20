from django.urls import path


from citizen.views import submit_report,feedback_survey

urlpatterns = [
    path('report', submit_report, name='report'),
    path('feedback-survey',feedback_survey, name='feedback'),
   
]