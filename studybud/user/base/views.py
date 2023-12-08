from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.db.models import Q 

# from django.contrib.auth.models import User # loginPage用 (removed)
from django.contrib import messages # loginPage用
from django.contrib.auth import authenticate, login, logout # loginPage/logoutPage

from .models import Room, Topic, Message, User 
from .forms import RoomForm, RoomFormM, UserForm, MyUserCreationForm #  

from django.contrib.auth.decorators import login_required 

# from django.contrib.auth.forms import UserCreationForm # 刪除

# Create your views here.

# rooms = [
#     {'id':1, 'name': 'Lets learn python!'},
#     {'id':2, 'name': 'Design with me'},
#     {'id':3, 'name': 'Frontend developers'},
# ]

def loginPage(request):
    page = 'login' # 
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # username = request.POST.get('username').lower() # 配合registerPage所需
        email = request.POST.get('email').lower() # 
        password = request.POST.get('password')

        try:
            # user = User.objects.get(username=username)
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        # user = authenticate(request, username=username, password=password)
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
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

    # form = UserCreationForm() # 取消
    form = MyUserCreationForm() # 新增 

    if request.method == 'POST':
        # form = UserCreationForm(request.POST) # 取消
        form = MyUserCreationForm(request.POST) # 新增
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

    topics = Topic.objects.all()[0:5] #
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
        message = Message.objects.create(
            user = request.user, 
            room = room,
            body = request.POST.get('body') 
        )
        room.participants.add(request.user) # 
        return redirect('room', pk=room.id)

    # return render(request, 'base/room.html')
    return render(request, 'base/room.html', context)

def userProfile(request, pk): 
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
    topics = Topic.objects.all() # 新修

    if request.method == 'POST':
        """方法2"""
        topic_name = request.POST.get('topic') # 新增2
        topic, created = Topic.objects.get_or_create(name=topic_name) # 新增2

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

        """方法1"""
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False) 
        #     room.host = request.user 
        #     room.save() 
        #     # form.save()
        #     return redirect('home')
    
    """方法1"""
    # context = {'form': form}
    """方法2(新修＋新增2)"""
    context = {'form': form, 'topics': topics } # 新修
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomFormM(instance=room)
    topics = Topic.objects.all() # 新增

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        """方法2"""
        topic_name = request.POST.get('topic') # 新增2
        topic, created = Topic.objects.get_or_create(name=topic_name) # 新增2
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

        """方法1"""
        # form = RoomFormM(request.POST, instance=room)
        # if form.is_valid():
        #     form.save()
        #     return redirect('home')
    # context = {'form': form}
    context = {'form': form, 'topics': topics, 'room': room } # 新修
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

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        # form = UserForm(request.POST, instance=user)
        form = UserForm(request.POST, request.FILES, instance=user) #
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    return render(request, 'base/update-user.html', {'form': form})

def topicsPage(request):
    # topics = Topic.objects.filter() 

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})

