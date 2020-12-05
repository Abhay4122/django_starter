from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from ckeditor.fields import RichTextField

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **other):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **other)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **other):
        if not email:
            raise ValueError(_('You must provide an email address'))

        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)
        other.setdefault('is_active', True)

        if other.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned to is_staff = True.'))

        if other.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be assigned to is_superuser = True'))

        user = self.model(email=self.normalize_email(email), **other)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_('email address'), max_length=150, unique=True)
    name = models.CharField(_('name'), max_length=150)
    contact = models.CharField(_('contact'), max_length=15, null=True, blank=True)
    bio = models.TextField(_('about user'), max_length=500, blank=True, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    doj = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []    # ask fields in CLI when createsuperuser command run. Email & Password are required by default.

    def __str__(self):
        return self.email


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null=True)
    male = models.BooleanField(default=False)
    bio = RichTextField(default='')
    doj = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
