from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
from .models import User

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            
            # Redirect based on user type
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def patient_dashboard(request):
    if request.user.user_type != 'patient':
        messages.error(request, 'You are not authorized to view this page!')
        return redirect('home')
    
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/patient_dashboard.html', context)

@login_required
def doctor_dashboard(request):
    if request.user.user_type != 'doctor':
        messages.error(request, 'You are not authorized to view this page!')
        return redirect('home')
    
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/doctor_dashboard.html', context)
