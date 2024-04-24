from django.urls import path  # type: ignore
from . import views
urlpatterns = [
    path('', views.test),
    path('student', views.student),
    path('index', views.index),

]
