import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from student_app.models import *
import os
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse
from .forms import StudentCreateForm, StudentEditForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def student(request):
    return render(request, 'student.html')


def home(request):
    return render(request, 'home.html')


def user_signup(request):
    return render(request, 'student.html')


@csrf_exempt
def set_present(request):
    if request.method == 'POST':
        student_id = request.POST.get('studentId')
        student = Student.objects.get(id=student_id)
        student.present = 'yes'
        student.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failed'})


def student_signup(request):
    # extracting form data from the request
    studentName = request.POST.get('studentName')
    department = request.POST.get('department')
    section = request.POST.get('section')
    rollNo = request.POST.get('rollNo')
    emailId = request.POST.get('emailId')
    collegeId = request.POST.get('collegeId')
    password = request.POST.get('password')
    present = 'no'

    # try to get a student with the given collegeId
    student, created = Student.objects.get_or_create(
        collegeId=collegeId,
        defaults={
            'studentName': studentName,
            'department': department,
            'section': section,
            'rollNo': rollNo,
            'emailId': emailId,
            'password': password,
            'present': present
        }
    )

    if created:
        return redirect('../studentLogin')
    else:
        return HttpResponse('A student with this collegeId already exists.')


def student_login(request):
    return render(request, 'studentLogin.html')


def student_log(request):

    a = request.POST.get('collegeId')
    b = request.POST.get('password')

    if Student.objects.filter(collegeId=a, password=b):
        u = Student.objects.filter(collegeId=a, password=b)
        return render(request, 'studentDashboard.html', {'students': u})

    else:
        return redirect('../studentLogin')


def faculty_log_page(request):
    return render(request, 'facultyLogin.html')


def faculty_log(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('../facultylogpage')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Nigga')
            return redirect('../facultylogpage')
        else:
            login(request, user)
            return redirect('../admin-dashboard')

    return render(request, 'facultyLogin.html')


def faculty_register(request):
    return render(request, 'facultyRegister.html')


def faculty_reg(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('../faculty-register')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

        user.set_password(password)
        user.save()
        messages.info(request, 'Account created sucessfully')

        return redirect('../facultylogpage')

    return redirect('../faculty-register')


def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all()
    })


def view_student(request, id):
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            new_studentName = form.cleaned_data['studentName']
            new_department = form.cleaned_data['department']
            new_section = form.cleaned_data['section']
            new_rollNo = form.cleaned_data['rollNo']
            new_emailId = form.cleaned_data['emailId']
            new_collegeId = form.cleaned_data['collegeId']
            new_password = form.cleaned_data['password']
            new_present = form.cleaned_data['present']

            new_student = Student(
                studentName=new_studentName,
                department=new_department,
                section=new_section,
                rollNo=new_rollNo,
                emailId=new_emailId,
                collegeId=new_collegeId,
                password=new_password,
                present=new_present
            )
            new_student.save()
            return render(request, 'add.html', {
                'form': StudentCreateForm(),
                'success': True
            })
    else:
        form = StudentCreateForm()
    return render(request, 'add.html', {
        'form': StudentCreateForm()
    })


def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentEditForm(instance=student)
    return render(request, 'edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
