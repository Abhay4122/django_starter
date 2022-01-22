from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, help_text='Student name')
    email = models.CharField(max_length=100, help_text='Student email')
    contact = models.CharField(max_length=100, help_text='Student contact')
    address = models.CharField(max_length=250, help_text='Student address')
    dob = models.DateField(verbose_name='Date of birth')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
