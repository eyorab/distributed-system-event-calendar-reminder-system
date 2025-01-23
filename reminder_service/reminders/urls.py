from django.urls import path
from .views import ReminderAPIView

urlpatterns = [
    path('api/reminders/', ReminderAPIView.as_view(), name='reminders'),
]
