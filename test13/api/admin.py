from django.contrib import admin
from .models import Survey, Question, DefaultAnswer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    fields = ('name', 'date_start', 'date_finish', 'description')
    list_display = ('name', 'date_start', 'date_finish')
    search_fields = ('name', 'date_start')
    # readonly_fields = ['date_start']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['date_start']
        return self.readonly_fields


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('text', 'type', 'survey')
    list_display = ('text', 'type', 'survey')
    search_fields = ('text', 'type', 'survey')


@admin.register(DefaultAnswer)
class DefaultAnswerAdmin(admin.ModelAdmin):
    fields = ('text', 'question')
    list_display = ('text', 'question')
    search_fields = ('text', 'question')
