from django.urls import path
from . import views
from .api_views import EventList, EventDetail

urlpatterns = [
    path("", views.eventCalendar, name="eventCalendar"),
    path("add-event/", views.eventForm, name="eventForm"),
    path("dashboard/", views.dashboardView, name="dashboard"),
    path("event-list/", views.eventView, name="eventView"),
    # path("update-event/", views.updateEvent, name="updateEvent"),
    # path("delete-event/", views.deleteEvent, name="deleteEvent"),
    # API endpoints
    path("api/events/", EventList.as_view(), name="event-list"),  # List all events or create an event
    path("api/events/update/", EventDetail.as_view(), name="event-update"),
    path("api/events/delete/<str:id>", EventDetail.as_view(), name="event-delete"),
]


