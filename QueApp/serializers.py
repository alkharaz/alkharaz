from rest_framework import serializers
from QueApp.models import QuestionsModel, AnswersModel, UsersAnswerModel
from django.db.models import Count

class Answersserializer(serializers.ModelSerializer):
     UsersAnswer = serializers.StringRelatedField(many=True)

     class Meta:
         model = AnswersModel
         fields = ['id','Question', 'Answer','UsersAnswer']


class CountAnswersSerializer(serializers.ModelSerializer):

     answersCount = serializers.SerializerMethodField(read_only=True)

     class Meta:
         model = AnswersModel
         fields = ['id','Answer','answersCount']

     def get_answersCount(self, obj):
        return obj.UsersAnswer.count()

class UsersAnswersSerializer(serializers.ModelSerializer):

     QuestionID = serializers.PrimaryKeyRelatedField(source='Answer.Question.id',read_only=True)
     Answers = serializers.SerializerMethodField('get_answers')
     QuestionTxt = serializers.StringRelatedField(source='Answer.Question',read_only=True)

     def get_answers(self, obj):
        queryset = AnswersModel.objects.filter(Question=obj.Answer.Question.id)
        serializer = CountAnswersSerializer(instance=queryset, many=True)
        return serializer.data
     
     class Meta:
         model = UsersAnswerModel
         fields = ['QuestionID','QuestionTxt','Answer', 'Answers']

class AnswersOnlySerializer(serializers.ModelSerializer):
     class Meta:
         model = AnswersModel
         fields = ['id','Answer']

class Questionserializer(serializers.ModelSerializer):
     ##Answers = serializers.StringRelatedField(many=True)
     QuestionAnswer = AnswersOnlySerializer(many=True, read_only=True)

     class Meta:
         model = QuestionsModel
         fields = ['id','Question','CorrectAnswer','QuestionAnswer']

    # This is to Remove Null Fields
     def to_representation(self, instance):
        rep = super().to_representation(instance)
        for field in self.fields:
            try:
                if rep[field] is None:
                    rep.pop(field)
            except KeyError:
                pass
        return rep
