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
                    <table border=1>
                        {}
                    </table>
                </body>
            </html>""".format(form(*args, **kwargs))
        return HttpResponse(html)
    return warp_html


@csrf_exempt
@decor_warp_html
def show_rooms(request):
    rooms = Room.objects.all()
    res = ""
    for room in rooms:
        res += """<tr><td><a href='/room/{}'>{}</a></td></tr>""".format(room.id, room.name)
    return res


@csrf_exempt
def details_room(request, id):
    pass




@csrf_exempt
def edit_room(request):
    pass

@csrf_exempt
def add_room(request):
    pass


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
def delete_room(request):
    pass



