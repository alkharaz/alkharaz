from django.db import models


# Create your models here.

class QuestionsModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    Question = models.CharField(max_length=200)
    CorrectAnswer = models.IntegerField()
    class Meta:
        verbose_name_plural = "Questions"
    
    def __str__(self):
        return self.Question

class AnswersModel(models.Model):
    Question = models.ForeignKey(QuestionsModel, related_name='QuestionAnswer', on_delete=models.CASCADE)
    Answer = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.Answer

class PushNotificationModel(models.Model):
    PushTitle = models.CharField(max_length=200,blank=True, default='')
    PushMsg = models.CharField(max_length=200,default='')
    class Meta:
        verbose_name_plural = "Push Notifictions Message"
        verbose_name = 'Push Notifiction'

    def __str__(self):
        return self.PushMsg

class UsersAnswerModel(models.Model):
    Answer = models.ForeignKey(AnswersModel, related_name='UsersAnswer', on_delete=models.CASCADE)
    RegistrationID = models.CharField(max_length=200)
    APNSDevice = models.CharField(max_length=200,default='no name')
    class Meta:
        verbose_name_plural = "Users Answer"

    def __str__(self):
        return self.RegistrationID
