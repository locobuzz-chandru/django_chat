from django.shortcuts import render
from ..models import Messages
from django.contrib.auth.decorators import login_required
from channels.db import database_sync_to_async


@login_required(login_url='/auth/login/')
def room(request, room_name):
    messages = Messages.objects.filter(group__name=room_name)
    print(messages)
    return render(request, "room.html", {"room_name": room_name,
                                         "username": request.user.username,
                                         "message_list": messages})


