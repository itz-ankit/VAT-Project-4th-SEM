from pyclbr import Class
from pyexpat import model
from django.db import models

# Create your models here.


class Student(models.Model):
    studentName = models.CharField(max_length = 50 )
    department = models.TextField(max_length= 50)
    section = models.CharField(max_length=50)
    rollNo = models.CharField(max_length=20)
    emailId = models.EmailField(max_length=100)
    collegeId = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    present = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)




class Student_admin(models.Model):
  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()

  def __str__(self):
    return f'Student_admin: {self.first_name} {self.last_name}'  