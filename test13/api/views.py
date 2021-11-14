from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import SurveySerializer, SurveyReportSerializer
from rest_framework import mixins
from django.core.serializers import serialize
from .models import Survey, Question, DefaultAnswer, Answer, SurveyReport
from django.forms.models import model_to_dict


# SurveysAdmin
class SurveysGet(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyReportPost(generics.ListCreateAPIView):
    queryset = SurveyReport.objects.all()
    serializer_class = SurveyReportSerializer



