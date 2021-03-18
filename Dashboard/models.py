from django.db import models
from QueApp.models import QuestionsModel
# Create your models here.

class DashboardModel(QuestionsModel):
    class Meta:
        proxy = True
        verbose_name = "Question Statistic"
        verbose_name_plural = "Questions Statistic"
    
    def do_something(self):
        pass
