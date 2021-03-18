from django.contrib import admin
from .models import QuestionsModel, AnswersModel, PushNotificationModel, UsersAnswerModel
from push_notifications.models import APNSDevice
from django.db.models.signals import post_save
# Register your models here.

class UsersAnswerAdmin(admin.ModelAdmin):
    model = AnswersModel
    list_display = ('id','Answer','APNSDevice','RegistrationID')

class UsersAnswerAdminLink(admin.TabularInline):
    model = UsersAnswerModel
    list_display = ('id','RegistrationID')

class AnswersAdmin(admin.ModelAdmin):
    inlines = [UsersAnswerAdminLink]
    class Meta:
        model = AnswersModel
    list_display = ('id','Answer')

class AnswersAdminLink(admin.TabularInline):
    model = AnswersModel
    list_display = ('id','Answer')

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswersAdminLink]
    class Meta:
        model = QuestionsModel
    list_display = ('id','Question','CorrectAnswer')

def Push_created(sender, instance, **kwargs):
        if kwargs['created']:
            APNSDevice.objects.all().send_message(message={"title":str(instance.PushTitle),"body" : str(instance.PushMsg)})

class PushNotificationAdmin(admin.ModelAdmin):
    class Meta:
        model = PushNotificationModel
        post_save.connect(Push_created, sender=PushNotificationModel)
    list_display = ('id','PushTitle','PushMsg')


admin.site.register(QuestionsModel, QuestionsAdmin)
admin.site.register(AnswersModel, AnswersAdmin)
admin.site.register(PushNotificationModel,PushNotificationAdmin)
admin.site.register(UsersAnswerModel, UsersAnswerAdmin)
