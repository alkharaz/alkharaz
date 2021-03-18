from django.urls import path, include
from .views import QuestionsView,UsersAnswerView
from push_notifications.api.rest_framework import APNSDeviceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('device/apns', APNSDeviceViewSet)

urlpatterns = [
    path('Question',QuestionsView.as_view()),
    path('Answer',UsersAnswerView.as_view()),
    path('', include(router.urls)),
]
