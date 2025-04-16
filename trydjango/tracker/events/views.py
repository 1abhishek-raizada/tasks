import datetime
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render
from .models import Event
# Create your views here.

def dashboard(request):
    today=datetime.date.today()
    start_date=today-datetime.timedelta(days=6)

    events = Event.objects.filter(timestamp__date__gte=start_date) \
        .annotate(day=TruncDate('timestamp')) \
        .values('day') \
        .annotate(count=Count('id')) \
        .order_by('day')
   



    event_dict={item['day'].strftime("%Y-%m-%d"): item['count'] for item in events}
    labels=[]
    counts=[]
    for i in range(7):
        day=start_date + datetime.timedelta(days=i)
        day_str=day.strftime("%Y-%m-%d")
        labels.append(day_str)
        counts.append(event_dict.get(day_str,0))

    context={
        'labels':labels,
        'counts':counts
    }    

    return render(request,'events/dashboard.html',context)





def home(request):
    return render(request,'events/index.html')