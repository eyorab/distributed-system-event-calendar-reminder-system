from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
from .mongodb import MongoDBClient
from datetime import datetime
from django.forms import ValidationError
from .models import Event


mongo_client = MongoDBClient()
collection = mongo_client.get_collection("events")

 
class EventCalendar(HTMLCalendar):
    def __init__(self, events=None):
        super(EventCalendar, self).__init__()
        self.events = events
 
    def formatday(self, day, weekday, events):
        """
        Return a day as a table cell.
        """
        events_from_day = events.filter(day__day=day)
        events_html = "<ul>"
        for event in events_from_day:
            events_html += event.get_absolute_url() + "<br>"
        events_html += "</ul>"
 
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)
 
    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s
 
    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
 
        events = Event.objects.filter(day__month=themonth)
 
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, events))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

class Event:
    def __init__(self, title, day, start_time, end_time, category, description):
        self.title = title
        self.day = day
        self.start_date = start_time
        self.end_date = end_time
        self.category = category
        self.description = description

    def get_absolute_url(self):
        return f'<a href="/events/{self.id}/">{self.title}</a>'

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True

        return overlap

    # def clean(self):
    #     if self.end_time <= self.start_time:
    #         raise ValidationError('Ending times must after starting times')

    #     events = Event.objects.filter(day=self.day)
    #     if events.exists():
    #         for event in events:
    #             if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
    #                 raise ValidationError( 
    #                   events = list(collection.find({}))  'There is an overlap with another event: ' + str(event.day) + ', ' + str(
    #                         event.start_time) + '-' + str(event.end_time))
                    
 
    def __str__(self):
        return self.title