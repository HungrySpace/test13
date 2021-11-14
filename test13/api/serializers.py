from datetime import datetime
from rest_framework import serializers
from .models import Survey, Question, DefaultAnswer, Answer, SurveyReport
from rest_framework.response import Response


class DefaultAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultAnswer
        fields = ("id", "text",)


class QuestionSerializer(serializers.ModelSerializer):
    default_answers = DefaultAnswerSerializer(required=True, many=True)

    class Meta:
        model = Question
        fields = ("id", "text", "type", 'default_answers',)


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(required=True, many=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'date_start', 'date_finish', 'description', 'questions')

    def to_representation(self, instance):
        print(instance)
        print(instance.date_finish, datetime.date(datetime.now()), instance.date_start)
        if instance.date_finish >= datetime.date(datetime.now()) >= instance.date_start:
            ret = super().to_representation(instance)
            return ret


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'user_answer', 'chosen_answer', 'report')


class SurveyReportSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(required=True, many=True)
    # survey = SurveySerializer(required=False, many=False)

    class Meta:
        model = SurveyReport
        fields = ('id', 'user', 'survey', 'answers')

    def to_representation(self, instance):
        print(instance)
        ret = super().to_representation(instance)
        return ret

    def create(self, validated_data):
        for answers in validated_data['answers']:
            Answer.objects.create(**answers)
        SurveyReport.objects.create(user=validated_data['user'], survey=validated_data['survey'])
        return validated_data
