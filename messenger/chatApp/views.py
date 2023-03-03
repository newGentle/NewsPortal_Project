from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView 
from rest_framework.response import Response
from .serializers import MessagesSerializer, RoomsSerializer
# from rest_framework.decorators import 
from .models import Messages, Rooms
# Create your views here.

class MessagesApiView(ListAPIView):
    def get(self, request):
        msg = Messages.objects.all()
        return render(request, template_name='index.html',context={'msg': MessagesSerializer(msg, many=True).data})

    def post(self, request):
        serializer = MessagesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return render(request, template_name="index.html" )

    def put(self, response):
        pass

class RoomsApiView(APIView):
    def get(self, request):
        rooms = Rooms.objects.all()
        return Response({'rooms': RoomsSerializer(rooms, many=True).data})


class RoomApiView(APIView):
    def get(self, request, slug):
        room = Rooms.objects.get(slug=slug)
        return Response({'room': RoomsSerializer(room).data})

def index(request):
    return render(request, template_name='index.html')

# @login_required
def room(request, slug):
    room = Rooms.objects.get(slug=slug)
    return render(request, template_name='room.html', context={'chat_room': room})