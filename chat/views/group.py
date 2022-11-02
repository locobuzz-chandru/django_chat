from ..models import Group
from user.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


@login_required(login_url='/auth/login/')
def index(request):
    """Function to view groups"""
    try:
        group_list = Group.objects.filter(user=request.user)
        context = {'group_list': group_list}
        return render(request, 'index.html', context)

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


@login_required(login_url='/auth/login/')
def add_group(request):
    """Function to create group"""
    try:
        if request.method == 'POST':
            name = request.POST['name']
            Group.objects.create(name=name, user=request.user)
            messages.info(request, "GROUP CREATED SUCCESSFULLY")
            return redirect('index')
        return render(request, 'index.html')

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


@login_required(login_url='/auth/login/')
def delete_group(request, id):
    """Function to delete the group"""
    try:
        group = Group.objects.get(pk=id, user=request.user)
        group.delete()
        messages.info(request, "GROUP DELETED SUCCESSFULLY")
        return redirect('index')

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


@login_required(login_url='/auth/login/')
def edit_group(request, id):
    """Function to select the group name to update the group name """
    try:
        select_group = Group.objects.get(pk=id, user=request.user)
        context = {'select_group': select_group}
        return render(request, 'index.html', context)

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


@login_required(login_url='/auth/login/')
def update_group(request, id):
    """Function to update the group name"""
    try:
        group = Group.objects.get(pk=id, user=request.user)
        group.name = request.POST['name']
        group.save()
        messages.info(request, "GROUP UPDATED SUCCESSFULLY")
        return redirect('index')

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


@login_required(login_url='/auth/login/')
def get_members(request, group_id):
    """Function to display members and users"""
    try:
        group = Group.objects.get(id=group_id, user=request.user)
        context = {'member_list': group.members.all(), 'user_list': User.objects.all().exclude(id=request.user.id),
                   'group_id': group_id}
        return render(request, 'members/members.html', context)

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


@login_required(login_url='/auth/login/')
def add_member(request, group_id, user_id):
    """Function to add member"""
    try:
        group = Group.objects.get(id=group_id, user=request.user)
        user = User.objects.get(id=user_id)
        group.members.add(user)
        return redirect('members', group_id=group_id)

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


@login_required(login_url='/auth/login/')
def remove_member(request, group_id, user_id):
    """Function to remove member from the group"""
    try:
        group = Group.objects.get(id=group_id, user=request.user)
        user = User.objects.get(id=user_id)
        group.members.remove(user)
        print(group.members.all())
        return redirect('members', group_id=group_id)

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)
