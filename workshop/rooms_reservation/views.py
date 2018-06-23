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
        res += """<tr><td><a href='/room/{}'>{}</a> <a href='/room/modify/{}' style='color: red;'>
                        <small>Edytuj</small></a><br>
                        <a href='/room/delete/{}' style='color: black;'>Usuń</a></td></tr></form>""".format(room.id,
                                                                                                            room.name,
                                                                                                            room.id,
                                                                                                            room.id)
    res += "</table><br>"
    res += """<a href='/room/new'>Dodaj salę</a>
              <a href='/search/'>Wyszukaj salę</a>"""
    return res


@csrf_exempt
def details_room(request, id):
    room = Room.objects.get(id=id)

    answer = """
            <div align="center">
                    <h1>Nazwa sali: {}</h1><br>
                    <h3>Pojemność: {}</h3><br>
            """.format(room.name, room.capacity)
    if room.projector:
        answer += "<h3>Posiada rzutnik</h3><br>"
    else:
        answer += "<h3>Nie posiada rzutnika</h3><br>"
    answer += """
            </div>
            <div align="center">
            """
    try:
        reserved = Reservation.objects.get(room_id=id)
        answer += "Sala zarezerwowana na dni:<br>"
        for res in reserved:
            answer += "<ul><li>{}</li></ul><br>".format(res.date)
    except Reservation.DoesNotExist:
        answer += "Brak rezerwacji"
    answer += "</div>"
    return HttpResponse(answer)



@csrf_exempt
def edit_room(request, id):
    room = Room.objects.get(id=id)
    response = HttpResponse()
    if request.method == 'GET':
        form = """<html><body><form action='#' method='POST'>"""
        form += """Zmień dane sali {} <br><br>""".format(room.name)
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
        form += "</form></body><//html>"
        response.write(form)
    else:
        name = request.POST.get('room_name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector')
        if projector is not None:
            projector = True
        else:
            projector = False
        room.name = name
        room.capacity = capacity
        room.projector = projector
        room.save()
        response.write("Zmieniono dane sali {}".format(room.name))

    return response

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
        form += "</form></body></html>"
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
@decor_warp_html
def search_room(request):
    rooms = Room.objects.all()
    form = """
             <form action="#" method="POST">
                <label>
                    Minimalna pojemność sali:
                    <input type="number" name="capacity" width=10>
                </label>
                <label>
                    <br><br>
                    Data:
                    <input name="day" size="5" placeholder="day">
                    <input name="month" size="5" placeholder="month">
                    <input name="year" size="5" placeholder="year">
                </label>
                <label>
                    <br><br>
                    Rzutnik:
                    <select name="projector">
    		            <option value="True">Tak</option>
    		            <option value="False">Nie</option>
                    </select>
                </label>
                <br><br>
                <input type="submit" value="Szukaj">
            </form>
            """
    if request.method == 'GET':
        return form
    elif request.method == 'POST':
        my_day = int(request.POST.get("day"))
        my_month = int(request.POST.get("month"))
        my_year = int(request.POST.get("year"))
        capacity = int(request.POST.get("capacity"))
        projector = bool(request.POST.get("projector"))
        date = datetime(year=my_year, month=my_month, day=my_day)
        rooms_list = []
        for room in rooms:
            if room.projector == projector and room.capacity >= capacity:
                rooms_list.append(room)
            for good_room in rooms_list:
                if good_room.date == date:
                    rooms_list.pop(good_room)
        return rooms_list




@csrf_exempt
def delete_room(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    answer = "Sala {} usunięta".format(room.name)
    return HttpResponse(answer)

