from django.shortcuts import render

def index(request):
    return render(request, 'event/index.html')

def events(request):
    return render(request, 'event/events.html')

def submit_event(request):
    return render(request, 'event/submit_event.html')
