from django.shortcuts import render


def chat_room_view(request, room_name):
    return render(request, 'room.html')
