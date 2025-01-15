from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from .models import Message

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat_home')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat_home')
    return render(request, 'chat/login.html')

@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/chat_home.html', {'users': users, 'current_user': request.user})

@login_required
def get_chat_history(request, user_id):
    try:
        other_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'messages': []})
    # Get messages either sent from the current user to the other user or vice versa.
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) | Q(sender=other_user, receiver=request.user)
    ).order_by('timestamp')
    messages_list = [{
        'sender_username': msg.sender.username,
        'content': msg.content,
        'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    } for msg in messages]
    return JsonResponse({'messages': messages_list})

def user_logout(request):
    logout(request)
    return redirect('login')

def landing_page(request):
    return render(request, 'chat/landing_page.html')
