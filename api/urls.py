from django.urls import path
from .views import *

urlpatterns = [
    path('student', student.as_view(), name='student'),
]
