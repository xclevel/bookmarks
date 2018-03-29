from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from account.form import UserRegistrationForm
from account.models import Profile
from .form import  UserRegistrationForm,UserEditForm, ProfileEditForm

@login_required
def dashboard(request):
    return render(request,'registration/dashboard.html',{'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'registration/register_done.html',
                          {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user)
    return render(request,'registration/edit.html',{'user_form': user_form,'profile_form': profile_form})