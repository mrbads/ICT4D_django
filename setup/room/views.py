from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import FloorSize, Calculated

# Create your views here.
def index(request):
    room_list = FloorSize.objects.order_by('-name')
    context = {'room_list': room_list,}
    return render(request, 'room/index.html', context)

def detail(request, room_id):
    try:
        room = FloorSize.objects.get(pk=room_id)
    except:
        raise Http404("Room does not exist")
    return render(request, 'room/detail.html', {'room': room})

def result(request, room_id):
    response = "You're looking at the results of room %s."
    return HttpResponse(response % room_id)

def input(request, room_id):
    room = get_object_or_404(FloorSize, pk=room_id)
try:
        selected_room = room.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        raise
    return HttpResponse("You're inputting on room %s." % room_id)
