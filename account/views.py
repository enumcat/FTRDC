from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=64)
    username = forms.CharField(max_length=64)
    password1 = forms.CharField(max_length=256)
    password2 = forms.CharField(max_length=256)

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=64)
    password = forms.CharField(max_length=256)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'account/login.html',
                          {'wrong': True, 'wrongMes': _("Wrong input.")})
        if not User.objects.filter(email=request.POST['email']):
            return render(request, 'account/login.html',
                          {'wrong': True, 'wrongMes': _("Wrong email address.")})
        user = User.objects.get(email=request.POST['email'])
        if not check_password(request.POST['password'], user.password):
            return render(request, 'account/login.html',
                          {'wrong': True, 'wrongMes': _("Wrong password.")})
        #Login
        request.session['id'] = user.pk
        request.session['username'] = user.username
        return HttpResponseRedirect(reverse('index'))
    else :
        try:
            user = User.objects.get(pk=request.session['id'])
            request.session['username'] = user.username
            return HttpResponseRedirect(reverse('index'))
        finally:
            return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'account/register.html',
                          {'wrong': True})
        if User.objects.filter(email=request.POST['email']):
            return render(request, 'account/register.html',
                          {'wrong': True, 'wrongMes': _("Email has been used.")})
        if User.objects.filter(username=request.POST['username']):
            return render(request, 'account/register.html',
                          {'wrong': True, 'wrongMes': _("Username has been used.")})
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'account/register.html',
                          {'wrong': True, 'wrongMes ': _("Different passwords.")})

        # Create User
        user = User(email=request.POST['email'], username=request.POST['username'],
                    password=make_password(request.POST['password1']))
        user.save()
        request.session['id'] = user.pk
        request.session['username'] = user.username
        return HttpResponseRedirect(reverse('index'))
    else :
        return render(request, 'account/register.html')

def logout(request):
    try:
        del request.session['id']
    finally:
        return HttpResponseRedirect(reverse('index'))
