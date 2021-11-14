from django.urls import path
from .views import SurveysGet, SurveyReportPost

urlpatterns = [
    # path('events', views.EventsViews.as_view()),
    path('api/surveys', SurveysGet.as_view()),
    path('api/SurveyReport', SurveyReportPost.as_view()),
]
