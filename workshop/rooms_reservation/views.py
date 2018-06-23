from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views import View
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta
from rooms_reservation.models import *
# Create your views here.


def decor_warp_html(form):
    def warp_html(*args, **kwargs):
        html = """
            <html>
                <body>
                    {}
                </body>
            </html>""".format(form(*args, **kwargs))
        return HttpResponse(html)
    return warp_html


@csrf_exempt
@decor_warp_html
def show_rooms(request):
    rooms = Room.objects.all()

    res = "<table border=1px>"
    for room in rooms:
        res += """<tr><td><a href='/room/{}'>{}</a> <a href='room/modify/{}' style='color: red;'>
                        <small>Edytuj</small></a></td></tr>""".format(room.id, room.name, room.id )
    res += "</table><br>"
    res += """<a href='/room/new'>Dodaj salę</a>
              <a href='/search/'>Wyszukaj salę</a>"""
    return res




@csrf_exempt
def details_room(request, id):
    pass



@csrf_exempt
def edit_room(request):
    pass

@csrf_exempt
def add_room(request):
    response = HttpResponse()
    if request.method == 'GET':
        form = """<html><body><form action='#' method='POST'>"""
        form += """<label> Nazwa sali:<br>
                           <input type='text' name='room_name'>
                           </label><br><br>"""
        form += """<label> Pojemność:<br>
                           <input type='number' name='capacity'>
                           </label><br><br>"""
        form += """<label> Projektor:<br>
                           <input type='checkbox' name='projector' value='projector'>
                           </label><br><br>"""
        form += "<input type='submit' value='wyślij'>"
        form += "</form>"
        response.write(form)
    else:
        name = request.POST.get('room_name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector')
        if projector is not None:
            projector = True
        else:
            projector = False
        Room.objects.create(name=name, capacity=capacity, projector=projector)
        response.write("Dodano salę")

    return response


@csrf_exempt
def search_room(request):
    pass

@csrf_exempt
def delete_room(request):
    pass