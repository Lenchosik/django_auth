from django.shortcuts import render
# главная страница
from django.shortcuts import render
def loginPage(request):
    return render(request, 'main/login.html')
def registerPage(request):
    return render(request, 'main/registration.html')