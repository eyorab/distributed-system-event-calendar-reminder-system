# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
 
class Event(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u'User ID', help_text=u'User ID', null=True)
    title = models.CharField(u'Title', help_text=u'Title', max_length=200,null=True)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_date = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_date = models.TimeField(u'Final time', help_text=u'Final time')
    category = models.CharField(u'Event Category', help_text=u'Event Category', max_length=100,default='personal')
    description = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
    

 
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
 
        return overlap
 
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
 
    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError('Ending times must after starting times')
 
        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_date, event.end_date, self.start_date, self.start_date):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_date) + '-' + str(event.end_date))


