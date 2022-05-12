from calendar import weekday
from cmath import phase
from hashlib import new
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from pkg_resources import safe_name
from .models import Mess 
from .models import Student
from .models import Hostels
from .models import Room

 

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html',{'name':'Muhammad Abu Huraira'})

def Student(request):
    return render(request, 'accounts/student.html')

def mess_manager(request):
    return render(request, 'accounts/mess_manager.html')

def resident_tutor(request):
    return render(request, 'accounts/resident_tutor.html')

def data(request):
    if request.method == 'POST':
        meal = request.POST['meal']
        price = request.POST['price']
        weekday = request.POST['weekday']
        servetime = request.POST['servetime']
        new_mess = Mess(meal=meal, price=price, weekday=weekday, servetime=servetime)
        
        
        new_mess.save()
        
        posts = Mess.objects.raw("select * from accounts_mess")
        
        print(posts)
        
        print(connection.queries)
        
        
    
    return render(request, 'accounts/data.html', {"Data" : posts})



def sadd(request):
    student_list = Student.objects.all()
        
        
    return render(request, 'accounts/sadd.html',
    {'student_list' : student_list})


def student_management(request):
    hostel_list = Hostels.objects.all()
    
        
    return render(request, 'accounts/student_management.html',
    {'hostel_list' : hostel_list})
    
    
