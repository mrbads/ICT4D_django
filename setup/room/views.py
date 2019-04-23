from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import FloorSize

# Create your views here.
class IndexView(generic.ListView):
    """docstring for IndexView."""
    template_name = 'room/index.html'
    context_object_name = 'room_list'

    def get_queryset(self):
        return FloorSize.objects.order_by('-name')

class DetailView(generic.DetailView):
    """docstring for DetailView."""
    model = FloorSize
    template_name = 'room/detail.html'

    def get_queryset(self):
        return FloorSize.objects.order_by('-name')

class ResultsView(generic.DetailView):
    """docstring for ResultsView."""
    model = FloorSize
    template_name = 'room/result.html'

# def index(request):
#     room_list = FloorSize.objects.order_by('-name')
#     context = {'room_list': room_list,}
#     return render(request, 'room/index.html', context)
#
# def detail(request, room_id):
#     try:
#         room = FloorSize.objects.get(pk=room_id)
#     except:
#         raise Http404("Room does not exist")
#     return render(request, 'room/detail.html', {'room': room})
#
# def result(request, room_id):
#     response = "You're looking at the results of room %s."
#     return HttpResponse(response % room_id)

def input(request, room_id):
    room = get_object_or_404(FloorSize, pk=room_id)
    try:
        selected_room = room.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'room/detail.html', {
            'name': name,
        })
    else:
        selected_room.save()
        return HttpResponseRedirect(reverse('room:result', args=(room.id, )))
