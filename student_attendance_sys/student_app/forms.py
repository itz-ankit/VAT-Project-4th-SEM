from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['studentName', 'department', 'section', 'rollNo', 'emailId', 'collegeId','password']
    labels = {
      'studentName': 'Student Name',
      'collegeId': 'College ID',
      'section': 'section',
      'rollNo': 'Roll Number',
      'emailId': 'Email',
      'department': 'Field of Study',
      'password' : 'Password'
    }
    widgets = {
      'studentName': forms.TextInput(attrs={'class': 'form-control'}),
      'collegeId': forms.NumberInput(attrs={'class': 'form-control'}),
      'section': forms.TextInput(attrs={'class': 'form-control'}),
      'rollNo': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'department': forms.TextInput(attrs={'class': 'form-control'}),
      'password': forms.PasswordInput(attrs={'class': 'form-control'})
    }