import re
from django.shortcuts import render , redirect
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from student_app.models import *
import os
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse
from .forms import StudentForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def student(request):
    return render(request, 'student.html')

def home(request):
    return render( request, 'home.html')

def user_signup(request):
    return render(request, 'student.html')

def student_signup(request):
        #extracting form data from the request
        studentName = request.POST.get('studentName')
        department = request.POST.get('department')
        section = request.POST.get('section')
        rollNo = request.POST.get('rollNo')
        emailId = request.POST.get('emailId')
        collegeId = request.POST.get('collegeId')
        password = request.POST.get('password')

        student = Student.objects.create(
             studentName = studentName,
             department = department,
             section = section,
             rollNo = rollNo,
             emailId = emailId,
             collegeId = collegeId,
             password = password,
        )
        return redirect('../studentLogin')

def student_login(request):
     return render(request, 'studentLogin.html')

def student_log(request):

    a = request.POST.get('collegeId')
    b = request.POST.get('password')

    if Student.objects.filter(collegeId = a, password = b):
        
        return render( request, 'studentDashboard.html' )
        
    else:
        return redirect('../studentLogin')


def student_dashboard(request):
     return render(request , 'studentDashboard.html')

def faculty_log_page(request):
    return render(request , 'facultyLogin.html')

def faculty_log(request):
     
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('../facultylogpage')
        
        user = authenticate(username=username, password = password)

        if user is None:
            messages.error(request, 'Nigga')
            return redirect('../facultylogpage')
        else:
            login(request, user)
            return redirect('../admin-dashboard') 

    return render(request, 'facultyLogin.html')


def faculty_register(request):
     return render(request , 'facultyRegister.html')

def faculty_reg(request):
     
     if request.method == "POST":
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = User.objects.filter(username = username)

          if user.exists():
               messages.info(request , 'Username already taken')
               return redirect('../faculty-register')  
          
          user = User.objects.create(
               first_name = first_name,
               last_name = last_name,
               username = username ,
               password = password
          )

          user.set_password(password)
          user.save()
          messages.info(request , 'Account created sucessfully')

          return redirect('../faculty-register')


     return redirect('../faculty-register')


def index(request):
  return render(request, 'index.html', {
    'students': Student_admin.objects.all()
  })

def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student_admin(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student_admin.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student_admin.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    student = Student_admin.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))