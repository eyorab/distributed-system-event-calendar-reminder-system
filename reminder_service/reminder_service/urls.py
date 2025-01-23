"""
URL Configuration for the Reminder Service

This file defines the URL patterns for the reminder service application. Each URL pattern maps an incoming URL to a specific view function or class-based view.

URL Patterns:

- `/`: Redirects to the home page.
- `/reminders/`: Displays a list of all reminders.
- `/reminders/create/`: Form for creating a new reminder.
- `/reminders/<int:reminder_id>/`: Displays details of a specific reminder.
- `/reminders/<int:reminder_id>/edit/`: Form for editing a reminder.
- `/reminders/<int:reminder_id>/delete/`: Deletes a reminder.
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('reminders/', include('reminders.urls')),
    path('admin/', admin.site.urls),
]
