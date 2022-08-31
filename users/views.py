from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket

# Create your views here.

def login(request):
    if request.method == 'POST':
        # initialise with data sent
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            # if such user exists(=got successfuly authenticated) 
            #   and not deleted(=is_active)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'form': form,

    }
    return render(request, "users/login.html", context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # 'messages' variable is automatically passed to context
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('users:login-page'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, "users/register.html", context)


# redirect address is set in settings file;
# probably, this decorator is not necessary if page is designed
# not to display profile button to anonymous user
@login_required
def profile(request):
    if request.method == 'POST':
        # information about the file being submitted 
        # is not sent in POST method
        form = UserProfileForm(request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile-page'))
    # fill the form with data from the user that makes a request
    form = UserProfileForm(instance=request.user)
    
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = 0
    total_sum = 0
    for basket in baskets:
        total_quantity += basket.quantity
        total_sum += basket.sum()
    context = {
        'form': form,
        'basket': baskets,
        'total_quantity': total_quantity,
        'total_sum': total_sum,

    }
    return render(request, "users/profile.html", context)


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

