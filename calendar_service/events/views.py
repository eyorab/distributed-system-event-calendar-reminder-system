from django.shortcuts import render
from .mongodb import MongoDBClient
from datetime import datetime

mongo_client = MongoDBClient()
collection = mongo_client.get_collection("events")

# Create your views here.
def eventCalendar(request):
    '''
    this is home page user could redirect whenever they logged in.
    so the login and signup algorithm is from the user service .
    this page based on the user service login page.
    whenever user logged in there it should redirect to events/  
    '''
    return render(request, 'home_page.html')

def eventForm(request):
    '''
    This is the form page where users can add events.
    Whenever the user clicks the add event button, it should navigate to this page.
    '''
    return render(request, 'add_event.html')

def dashboardView(request):
    '''
    this is the dashboard view where user could see the events.
    
    '''
    events = list(collection.find({}))
    for event in events:
        event['id'] = str(event['_id'])
    current_time = datetime.now()
    running_events = []
    upcoming_events = []
    completed_events = []
    for event in events:
        end_date = datetime.strptime(event['end_date'], '%Y-%m-%dT%H:%M:%SZ')
        start_date = datetime.strptime(event['start_date'], '%Y-%m-%dT%H:%M:%SZ')
        if end_date < current_time:
            completed_events.append(event)
        elif start_date < current_time < end_date:
            running_events.append(event)
        else:
            upcoming_events.append(event)
    context = {
        'running_events': running_events,
        'upcoming_events': upcoming_events,
        'completed_events': completed_events,
    }
    
    return render(request, 'dashboard.html',context)
    
    

def eventView(request):
    '''
    this is the event view where user could see the event.
    '''
    events = list(collection.find({}))
    for event in events:
        event['id'] = str(event['_id']) 
    return render(request, 'event_list.html', {'events': events})




