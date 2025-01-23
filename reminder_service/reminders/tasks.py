from celery import shared_task
from .models import Reminder
from django.utils.timezone import now
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

@shared_task
def send_reminders():
    reminders = Reminder.objects.filter(reminder_time__lte=now(), is_sent=False)
    for reminder in reminders:
        try:
            send_email(reminder.user.email, reminder.message)
            print(f"Sending reminder: {reminder.message}")
            reminder.is_sent = True
            reminder.save()
        except Exception as e:
            print(f"Failed to send reminder: {reminder.message}. Error: {e}")

def send_email(user_email, message):
    email = Mail(
        from_email='your_email@example.com',
        to_emails=user_email,
        subject='Reminder Notification',
        plain_text_content=message,
    )
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    sg.send(email)
