from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MyUser
from wardrobe.models import Wardrobe

from .forms import LoginForm,SignUpForm

from django.views.decorators.http import require_http_methods
from django.contrib.auth import login,logout,authenticate


# Create your views here.
@require_http_methods(['GET','POST'])
def welcome(request):
  if request.user.is_authenticated():
    return redirect('home')

  if request.method =='GET' :
    f=LoginForm();
    next_url=request.GET.get('next');
    return render(request,'base/welcome.html',{'nForm':f,'next':next_url});
  
  else:
    f=LoginForm(request.POST ) #now we get filled form
    next_url=request.POST.get('next')
    if f.is_valid():
      user=f.get_user()
      login(request,user)
      if not next_url:
        return redirect('home')
      else:
        return redirect(next_url)
    else:
      return render(request,'base/welcome.html',{'nForm':f})

def signupview(request):
  if request.user.is_authenticated():
    return redirect('home')
  
  if request.method =='GET' :
    f=SignUpForm();
    next_url=request.GET.get('next');
    return render(request,'base/signup.html',{'nForm':f,'next':next_url});
  else:
    f=SignUpForm(request.POST ) #now we get filled form
    next_url=request.POST.get('next')

    if f.is_valid():
      user=f.save()
      user.wardrobe=Wardrobe.objects.create(owner_id=user.id);
      user.save()
      return redirect('welcome')
    else:
      return render(request,'base/signup.html',{'nForm':f,'next':next_url})
  
@login_required
def home(request):
  return render(request,'account/home.html');

@login_required
def friends(request):
  return render(request,'account/friends.html');

def logoutview(request):
  logout(request)
  return redirect("welcome")




