from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import User

def home(request):
    count = User.objects.count()
    return render(request, "home.html", {
        'count': count
    })

def signup(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('home')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'