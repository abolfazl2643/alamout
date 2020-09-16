from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import User_Creation_Form,User_Update_Form
from .models import Profile
from django.contrib.auth.views import LoginView,LogoutView


class LoginViewClass(LoginView):
    model = User
    template_name = 'users/login.html'
    success_url = 'post_list'
class LogoutViewClass(LogoutView):
    model = User
    template_name = 'users/logout.html'


def user_creation_view(request):
    form = User_Creation_Form()
    if request.method == 'POST' :
        form = User_Creation_Form(request.POST)
        if form.is_valid :
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password = password )
            login(request,user)
            return redirect('post_list')
    else:
        form = User_Creation_Form()
    return render(request,'users/user_creation_form.html',{'form':form})            

def user_profile_view(request):

    user_object = request.user
    user = User.objects.get(username = user_object)

    context = {'user':user}
    return render(request,'users/profile.html',context)

def user_update_view(request):
    form = User_Update_Form()
    if request.method == 'POST':
        form = User_Update_Form(request.POST,instance = request.user)
        if form.is_valid :
            form.save()
            return redirect('profileview')
    else :
        form = User_Update_Form()
    return render(request,'users/userupdate.html',{'form':form})            