from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views import View
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta
from rooms_reservation.models import *
# Create your views here.



@csrf_exempt
def show_rooms(request):
    pass


@csrf_exempt
def details_room(request):
    pass

@csrf_exempt
def edit_room(request):
    pass

@csrf_exempt
def add_room(request):
    pass

@csrf_exempt
def search_room(request):
    pass

@csrf_exempt
def delete_room(request):
    pass


def decor_warp_html(form):
    def warp_html(*args, **kwargs):
        result = """
            <html>
                <body>
                    <table border=1>
                        {}
                    </table>
                </body>
            </html>""".format(form(*args, **kwargs))
        return HttpResponse(result)
    return warp_html

