from django.db import models
from django.utils.timezone import now

class Reminder(models.Model):
    user_id = models.CharField(max_length=255)  
    event_id = models.IntegerField() 
    reminder_time = models.DateTimeField()
    message = models.TextField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for User {self.user_id} at {self.reminder_time}"
