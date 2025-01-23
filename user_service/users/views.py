#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def signUp(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')
def profile(request):
    return render(request, 'user_profile.html')

