from django.contrib import admin
from .models import DashboardModel
from QueApp.models import QuestionsModel, AnswersModel, UsersAnswerModel
from django.db import models
from rest_framework import serializers


# Register your models here.

class DashboardAdmin(admin.ModelAdmin):
    class Meta:
        model = QuestionsModel
    change_list_template = 'admin/Dashboard_change_list.html'
    date_hierarchy = 'created'
    
    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response


        metrics = {
            'id' : models.F('id'),
            'totalAnswers' : models.Count('QuestionAnswer', distinct=True),
            'totalUsersAnswer' : models.Count('QuestionAnswer__UsersAnswer'),
        }

        response.context_data['summary'] = list(
            qs
            .values('Question')
	        .annotate(**metrics)
            .order_by('-id')
        )
        
        queryset = AnswersModel.objects.all()
        serializer = AnswersSerializer(queryset, many=True)
        response.context_data['answers'] = serializer.data
        
        return response

class AnswersSerializer(serializers.ModelSerializer):
    UsersAnswer = serializers.SerializerMethodField()

    class Meta:
        
        model = AnswersModel
        fields = ['Question','Answer','UsersAnswer']
    
    def get_UsersAnswer(self, obj):
        return obj.UsersAnswer.count()
        

admin.site.register(DashboardModel, DashboardAdmin)
