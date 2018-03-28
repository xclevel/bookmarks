from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from account.form import UserRegistrationForm


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
            return render(request,
                          'registration/register_done.html',
                          {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})