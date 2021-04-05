from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import requests

# Create your views here.
def index(request, show='', season = ''):
    episodes_bad = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    episodes_saul = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    breaking = {i : [x for x in episodes_bad if x['season'] == i ] for i in sorted(list(set(h['season'] for h in episodes_bad)))}
    saul = {i : [x for x in episodes_saul if x['season'] == i] for i in sorted(list(set(h['season'] for h in episodes_saul)))}
    return render(request, 'walt/index.html', {'breaking': breaking, 'saul': saul})

def edetail(request, episode_id):
    try:
        episode = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/' + str(episode_id)).json()
    except:
        raise Http404("There was an error retrieving information for that episode")
    return render(request, 'walt/edetail.html', {'episode': episode[0]})

def cdetail(request, character):
    try:
        info = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + character).json()
    except:
        raise Http404("There was an error retrieving information for that character")
    return render(request, 'walt/cdetail.html', {'character': info[0]})