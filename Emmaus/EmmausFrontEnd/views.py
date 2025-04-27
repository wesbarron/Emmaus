from django.shortcuts import render, HttpResponse
from .models import TodoItem, GatheringInformation, BoardMember, Pilgrim
from datetime import datetime, timedelta
from pytz import timezone
from django.db.models import Max

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def journey(request):
    return render(request, "journey.html")

def walk(request):
    return render(request, "walk.html")

def during_walk(request):
    return render(request, "during-walk.html")

def after_walk(request):
    return render(request, "after-walk.html")

def history(request):
    return render(request, "history.html")

def sponsorship(request):
    return render(request, "sponsorship.html")

def serve(request):
    return render(request, "serve.html")

def agape(request):
    return render(request, "agape.html")

def about(request):
    return render(request, "about.html")

def columbus(request):
    eastern = timezone('US/Eastern')
    fmt = '%B %d, %Y'
    loc_dt = eastern.localize(datetime.now()) - timedelta(hours=4)
    #print (loc_dt.strftime(fmt))
    events = GatheringInformation.objects.all().filter(cluster="Columbus", date__gte = loc_dt.strftime(fmt))
    return render(request, "columbuscluster.html", {'gatheringinfo' : events})

def manchester(request):
    eastern = timezone('US/Eastern')
    fmt = '%B %d, %Y'
    loc_dt = eastern.localize(datetime.now()) - timedelta(hours=4)
    #print (loc_dt.strftime(fmt))
    events = GatheringInformation.objects.all().filter(cluster="Manchester", date__gte = loc_dt.strftime(fmt))
    return render(request, "manchestercluster.html", {'gatheringinfo' : events})

def phenixcity(request):
    eastern = timezone('US/Eastern')
    fmt = '%B %d, %Y'
    loc_dt = eastern.localize(datetime.now()) - timedelta(hours=4)
    #print (loc_dt.strftime(fmt))
    events = GatheringInformation.objects.all().filter(cluster="Phenix City", date__gte = loc_dt.strftime(fmt))
    return render(request, "phenixcitycluster.html", {'gatheringinfo' : events})

def board(request):
    eastern = timezone('US/Eastern')
    fmt = '%Y'
    loc_dt = eastern.localize(datetime.now()) - timedelta(hours=4)
    board = BoardMember.objects.all().filter(year = loc_dt.strftime(fmt))
    return render(request, "board.html", {'board' : board})

def pilgrim(request):
    wpilgrim = Pilgrim.objects.all().filter(walk_group = 'Women', walk_number = '39')
    mpilgrim = Pilgrim.objects.all().filter(walk_group = 'Men', walk_number = '39')
    walknumber = Pilgrim.objects.get(walk_number = Max('walk_number'))
    return render(request, "pilgrim.html", {'w_pilgrims' : wpilgrim, 'm_pilgrims' : mpilgrim, 'walk' : walknumber})