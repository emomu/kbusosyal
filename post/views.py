
from .models import Like ,  Dweet , Posted , Profile 
from .models import Profile as ProfileModel 
from .forms import DweetForm , CreateUserForm 
from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.exceptions import ValidationError


def giris(request):
    return render(request,"post/giris.html")

@login_required(login_url='dwitter:login')
def sitehakkinda(request):
    return render(request,"post/sitehakkinda.html")

@login_required(login_url='dwitter:login')
def posted(request):
    qs = Posted.objects.all()
    userp = request.user

    context = {
        'qss': qs,
        'userp' : userp,

    }

    return render(request,"post/yurtlar.html" , context )


@login_required(login_url='dwitter:login')
def kesfet(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:kesfet")
    qs = Dweet.objects.all()
    user = request.user

    context = {
        'qs': qs,
        'user' : user,
        'form' : form,

    }

    return render(request,"post/kesfet.html" , context )


@login_required(login_url='dwitter:login')
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_save_id = request.POST.get('post_id')
        post_dweet = Dweet.objects.get(id =post_save_id)

        if user in post_dweet.liked.all():
            post_dweet.liked.remove(user)
        else:
            post_dweet.liked.add(user)

        like , created = Like.objects.get_or_create(user=user , post_save_id=post_save_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='dwitter:login')
def profile_list_query(request):
    if 'user' in request.GET and request.GET['user']:
        user = request.GET['user']
        if user:
            profiles = Profile.objects.filter(user__username__icontains=user)
            return render(request, 'post/aramasonucu.html' , {'profiles' : profiles})
        else:
            print("Aranılan sonuç bulunamadı")
            return render(request , 'post/aramasonucu.html' , {})

    else:
        return render(request , 'post/aramasonucu.html' , {})


@login_required(login_url='dwitter:login')
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "post/profile_list.html", {"profiles": profiles})


@login_required(login_url='dwitter:login')
def follows_list(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "post/follows.html", {"profile": profile}) 


@login_required(login_url='dwitter:login')
def followed_list(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "post/followed.html", {"profile": profile}) 


@login_required(login_url='dwitter:login')
def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "post/profile.html", {"profile": profile})


def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('dwitter:kesfet')

        else:
            messages.info(request,'kullanıcı adı ya da şifren yanlış.')

    
    context={}
    return render(request,'post/login.html')



@login_required(login_url='dwitter:login')
def logoutt(request):
    logout(request)
    return redirect('dwitter:login')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'hesabın başarıyla oluşturuldu ' + user)
            return redirect('dwitter:login')


    context = {
        'form' : form
    }
    return render(request,'post/register.html' ,context)




