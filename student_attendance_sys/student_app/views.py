from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from student_app.models import *
import os
# Create your views here.
def test(request):
    return HttpResponse('testing the page')


def index(request):
    return render(request, 'index.html')

def student(request):
    return render(request, 'student.html')

