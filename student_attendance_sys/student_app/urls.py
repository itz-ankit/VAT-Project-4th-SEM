from django.urls import path  # type: ignore
from . import views
urlpatterns = [
    path('', views.home , name='home-page'),
    path('student', views.student),
    path('index', views.index),
    path('signup', views.user_signup ),
    path('studentSignup' , views.student_signup),
    path('studentLogin', views.student_login),
    path('studentLog', views.student_log),
    # path('studentDashboard' , views.student_dashboard),
    path('facultylogpage', views.faculty_log_page ),
    path('faculty-log', views.faculty_log),
    path('faculty-register', views.faculty_register),
    path('faculty-reg', views.faculty_reg),
    # path('admin-dashboard', views.admin_dashboard ),

    path('admin-dashboard', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('setPresent/<int:id>', views.set_present, name='setPresent')
]
