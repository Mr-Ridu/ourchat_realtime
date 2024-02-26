from django.shortcuts import render, redirect ,HttpResponse
from django.http import JsonResponse
from .models import room_details,messege_details
from datetime import datetime,timedelta
from django.utils import timezone
from django.contrib import messages

# for home
def Ourchat(request):
    return render(request, 'home.html')


# for getting room
def getroom(request): 
    if request.method == 'POST':
        room_name = request.POST['room_name']
        reffer_code = request.POST['reffer_code']
        username = request.POST['username']
        showmessage = messege_details.objects.filter(m_room=room_name)
        if not room_name or not reffer_code or not username:
            messages.error(request,"Username or Roomname Invalid")
            return redirect('/')
        if room_details.objects.filter(room_name=room_name).exists():
            #thetime = timezone.now() - timedelta(minutes=1)
            #messege_details.objects.filter(m_time__lt=thetime).delete()
            context ={'room_name':room_name,'username':username,'showmessage':showmessage}
            return render(request,'room.html',context)
        else:
            createroom= room_details(room_name=room_name,reffer_code=reffer_code,username=username)
            createroom.save()
            messages.success(request, "Room Created")
            context ={'room_name':room_name,'username':username,'showmessage':showmessage}
            return render(request,'room.html',context)


 
    
def send(request):
    current_time = timezone.now()
    if request.method=='POST':
        username = request.POST['username']
        room_name = request.POST['room_name']
        message = request.POST['message']
        messege_details.objects.create(m_user=username,messege=message,m_room=room_name,m_time=current_time)
        p = messege_details.objects.filter(m_room=room_name).values()
        a=list(p)
        return JsonResponse({'ok':a})
    return JsonResponse({'notok':'not ok'})

    
def get_messages(request,room_name):
    room = messege_details.objects.filter(m_room=room_name).values()
    a=list(room)
    return JsonResponse({'messages':a})


def reload(request, room_name,username):
    
    showmessege= messege_details.objects.filter(m_room=room_name)

    context = {
        'room_name': room_name, 'showmessage': showmessege,'username':username
    }
    return render(request, 'room.html', context)


# def delmsg(request):
#     thetime = datetime.now()- timedelta(minutes=1)
#     details = messege_details.objects.all()
#     for time in  details.m_time:
#         if time <= thetime:
#             details.m_time.delete()
