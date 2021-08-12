from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import pgettext_lazy

from .models import Profile
from .forms import ProfileForm



def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            login(request, user) 
            print(user)
            messages.success(request, f' welcome {username} !!') 
            return redirect('profile-detail',pk=user.pk) 
        else: 
            messages.info(request, f'account does not exit plz sign in') 
    form = LoginForm()
    ctx = {"form":form}
    return render(request,'login.html',ctx)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/account/login/")
def profile_update(request,pk):
    user = get_object_or_404(User,pk=pk)
    profile = get_object_or_404(Profile,user=user)
    return _profile_edit(request,profile)


@login_required(login_url="/account/login/")
def profile_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    ctx = {"profile":profile}
    return render(request,'profile.html',ctx)


@login_required(login_url="/account/login/")
def _profile_edit(request, profile):
    form = ProfileForm(request.POST or None,request.FILES or None, instance=profile,user=request.user)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy("Dashboard message", "Saved Profile")
        messages.success(request, msg)
        return redirect("profile-detail", pk=profile.user.pk)
    ctx = {"profile": profile, "form": form}
    return render(request, "profile_form.html", ctx)


