from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import QuestionsModel, UsersAnswerModel
from . import serializers


class UsersAnswerView(APIView):

    def post(self,request):
        serializer = serializers.UsersAnswersSerializer(data=request.data)

        #queryset = UsersAnswerModel.objects.last()
        #serializer2 = serializers.UsersAnswersSerializer(queryset)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        

class QuestionsView(APIView):
    
    def get(self, request):

        queryset = QuestionsModel.objects.last()
        serializer = serializers.Questionserializer(queryset)

#        for filed_name,field_value in serializer.fields.items():
#            print(filed_name)
#            
#            if serializer.data.get(filed_name) is None:
#                print(serializer.data.get(filed_name))

        return Response(serializer.data)
