from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myview(request):
    # get value from key 'num_visits' if not return default 0 if not in dic
    num_visits = request.session.get('num_visits', 0) + 1
    # store the session key value 
    request.session['num_visits'] = num_visits
    # if number of visits value is more than 5
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse(f'view count={num_visits}')
    resp.set_cookie('dj4e_cookie', 'd01d0807', max_age=1000)
    return resp
