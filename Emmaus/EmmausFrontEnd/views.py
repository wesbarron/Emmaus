from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem, GatheringInformation, BoardMember, Pilgrim, Event
from datetime import datetime, timedelta
from pytz import timezone
from django.db.models import Max
from .forms import BoardMembers, Clusters
from django.urls import reverse

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
    # eastern = timezone('US/Eastern')
    # fmt = '%Y'
    # loc_dt = eastern.localize(datetime.now()) - timedelta(hours=4)
    board = BoardMember.objects.all() #.filter(year = loc_dt.strftime(fmt))
    return render(request, "board.html", {'board' : board})

def pilgrim(request):
    wpilgrim = Pilgrim.objects.all().filter(walk_group = 'Women', walk_number = '39')
    mpilgrim = Pilgrim.objects.all().filter(walk_group = 'Men', walk_number = '39')
    walknumber = Pilgrim.objects.get(walk_number = Max('walk_number'))
    return render(request, "pilgrim.html", {'w_pilgrims' : wpilgrim, 'm_pilgrims' : mpilgrim, 'walk' : walknumber})

def event(request):
    eastern = timezone('US/Eastern')
    fmt = '%B %d, %Y'
    wloc_dt = eastern.localize(datetime.now()) - timedelta(hours=4) - timedelta(hours=24)
    mloc_dt = eastern.localize(datetime.now()) - timedelta(hours=4) - timedelta(hours=24)
    #print (loc_dt.strftime(fmt))
    wevents = Event.objects.all().filter(walk_group="Women", end_date__gte = wloc_dt.strftime(fmt))
    mevents = Event.objects.all().filter(walk_group="Men", end_date__gte = mloc_dt.strftime(fmt))
    return render(request, "event.html", {'womensevent' : wevents, 'mensevent' : mevents})

def update_board(request):
    if request.method == "POST":
        form = BoardMembers(request.POST)
        if form.is_valid():
            position = form.cleaned_data["member_position"]
            name = form.cleaned_data["member_name"]
            context = {'MemberPosition': position, 'MemberName': name}
            eastern = timezone('US/Eastern')
            fmt = '%Y'
            loc_dt = eastern.localize(datetime.now()) - timedelta(hours=4)
            rec = BoardMember.objects.get(board_position=position)
            rec.member = name #Corey Salzman
            rec.year = loc_dt.strftime(fmt)
            rec.save()
            #url = reverse('board_confirmation', args=[position, name])
            #return redirect('manage_board_confirmation')
            return render(request, 'manage_board_confirmation.html', context)
        else:
            return render(request, 'manage_board.html', {'form': form})
    else:
        form = BoardMembers()
        return render(request, 'manage_board.html', {'form': form})
    
def board_confirmation(request, position, name):
    context = {'BoardPosition': position, 'BoardName': name}
    return render(request, 'manage_board_confirmation.html', context)

def add_cluster(request):
    if request.method == "POST":
        form = Clusters(request.POST)
        if form.is_valid():
            location = form.cleaned_data["location"]
            date = form.cleaned_data["date"]
            context = {'Location': location, 'Date': date}
            # eastern = timezone('US/Eastern')
            # fmt = '%B %d, %Y'
            # loc_dt = eastern.localize(datetime.now()) - timedelta(hours=4)
            # rec = BoardMember.objects.get(board_position=position)
            # rec.member = name #Corey Salzman
            # rec.year = loc_dt.strftime(fmt)
            # rec.save()
            #url = reverse('board_confirmation', args=[position, name])
            #return redirect('manage_board_confirmation')
            return render(request, 'manage_clusters_confirmation.html', context)
        else:
            return render(request, 'manage_clusters.html', {'form': form})
    else:
        form = Clusters()
        return render(request, 'manage_clusters.html', {'form': form})
    
def cluster_confirmation(request, location, date):
    context = {'Location': location, 'Date': date}
    return render(request, 'manage_clusters_confirmation.html', context)