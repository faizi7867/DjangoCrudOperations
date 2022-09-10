from django.http import HttpResponse
from django.shortcuts import render

from .models import Student


# Create your views here.
def home(request):
    return render(request, 'index.html')


def registerfunction(request):
    s = Student()
    s.name = request.POST['txtname']
    s.email = request.POST['txtemail']
    s.mobile = request.POST['txtmobile']
    s.subject = request.POST['txtsubject']
    s.password = request.POST['txtpassword']
    s.save()
    return render(request, 'login.html', {'name': s.name})


def loginfunction(request):
    email = request.POST['txtemail']
    password = request.POST['txtpassword']
    try:
        r = Student.objects.get(email=email, password=password)
        return HttpResponse('log in Sucessfull')
    except:
        print('data does not exist')
        msg = 'Invalid credentials?? please try again!!'
        return render(request, 'login.html', {'msg': msg})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def display(request):
    s = Student.objects.all()
    return render(request, 'display.html', {'slist': s})


def editfunction(request, id):
    s = Student.objects.get(id=id)
    if request.method == "POST":
        s.name = request.POST['username']
        s.email = request.POST['useremail']
        s.mobile = request.POST['usermobile']
        s.subject = request.POST['usersubject']
        s.password = request.POST['userpassword']
        s.save()
        x = Student.objects.all()
        return render(request, 'display.html', {'slist': x})
    return render(request, 'update.html', {'data': s})


def deletefunction(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    x = Student.objects.all()
    return render(request, 'display.html', {'slist': x})


