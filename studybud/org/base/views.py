from django.shortcuts import render, redirect  # render 為 default
# from django.shortcuts import HttpResponseRedirect # 自行使用為了測試
from django.http import HttpResponse 
from django.db.models import Q 

from django.contrib.auth.models import User # loginPage用
from django.contrib import messages # loginPage用
from django.contrib.auth import authenticate, login, logout # loginPage/logoutPage

from .models import Room, Topic, Message #  
from .forms import RoomForm 

from django.contrib.auth.decorators import login_required 

from django.contrib.auth.forms import UserCreationForm #

# Create your views here.

rooms = [
    {'id':1, 'name': 'Lets learn python!'},
    {'id':2, 'name': 'Design with me'},
    {'id':3, 'name': 'Frontend developers'},
]

def loginPage(request):
    page = 'login' # 
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower() # 配合registerPage所需
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            # User.objects.get(username=username) # 也可行
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # messages.success(request, 'Login Success!!', extra_tags='dragonball') # 自行添加
            login(request, user)
            return redirect('home') # 這裡用path中的name
            # return HttpResponseRedirect('/') # 這裡要用url。'/'代表 到home
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request): # 
    # page = 'register' # 實際上多餘
    # return render(request, 'base/login_register.html')
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registeration')

    return render(request, 'base/login_register.html', {'form': form})

def home(request):   
    q = request.GET.get('q')  if request.GET.get('q') != None else ''

    # rooms = Room.objects.all() 
    # rooms = Room.objects.filter(topic__name__icontains=q) # contains 則是使用case-sensitive
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        ) 

    topics = Topic.objects.all() 
    room_count = rooms.count()

    # room_messages = Message.objects.all() 
    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q)
        )

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count,
                'room_messages': room_messages} 
    return render(request, 'base/home.html', context)

# def room(request):
def room(request, pk):   
    # return HttpResponse('ROOM')

    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    print("room_id=",pk)
    # room_messages = room.message_set.all().order_by('-created') # 由新到舊
    room_messages = room.message_set.all() # Activity Feed時被修改

    participants = room.participants.all()  

    # context = {'room': room}
    context = {'room': room, 'room_messages': room_messages,
                'participants':participants 
            } 

    if request.method == 'POST':
        """方法一"""
        message = Message.objects.create(
            user = request.user, 
            room = room,
            body = request.POST.get('body') 
        )
        """方法二"""
        # message = Message(
        #     user = request.user, 
        #     room = room,
        #     body = request.POST.get('body') 
        # )
        # message.save()
        room.participants.add(request.user) # 
        return redirect('room', pk=room.id)

    # return render(request, 'base/room.html')
    return render(request, 'base/room.html', context)

def userProfile(request, pk): # 新增
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 
                'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def createRoom(request):
    
    # context = {}
    form = RoomForm() 
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            # room = form.save(commit=False) #
            # room.host = request.user #
            # room.save() # 
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':message})

def testTemp(request):
    print("testTemp>>")
    return render(request, 'test.html', {'rooms': rooms})