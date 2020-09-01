from django.shortcuts import render
from . models import Message
from . forms import MessageForm
from users.models import Account
from django.http import HttpResponseRedirect



# Create your views here.

def messageView(request,id):
    recipient = Account.objects.get(id=id)
    msgs = Message.objects.filter(sender=request.user,recipient=recipient) | Message.objects.filter(sender=recipient,recipient=request.user)

    if request.POST:
        messageForm = MessageForm(data=request.POST)
        if messageForm.is_valid():
            messageForm.save()
        return HttpResponseRedirect(request.path_info)

    messageForm = MessageForm(initial = {'sender': request.user, 'recipient': recipient})

    context = {
        'messageForm': messageForm,
        'msgs':msgs,
    }
    return render(request, 'message.html', context)



def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    users = room_name.split('_')
    for u in users:
        if u != request.user.username:
            recipient = Account.objects.get(username=u)
    msgs = Message.objects.filter(room_name=room_name)

    if request.POST:
        messageForm = MessageForm(data=request.POST)
        if messageForm.is_valid():
            messageForm.save()
        return HttpResponseRedirect(request.path_info)

    messageForm = MessageForm(initial = {'sender': request.user, 'recipient': recipient, 'room_name':room_name})

    context = {
        'msgs': msgs,
        'messageForm': messageForm,
        'room_name': room_name,
    }
    return render(request, 'chat/room.html', context)
