from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MemberManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Member(AbstractBaseUser):
    name = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100, default=None)
    email = models.EmailField(unique=True, default=None)
    status = models.CharField(max_length=25, default="Primary Member")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=100, default=None)
    emergency_contact_phone = models.BigIntegerField(default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'status', 'emergency_contact', 'emergency_contact_phone']

    def __str__(self):
        return self.email

class Bunk(models.Model):
    area = models.CharField(max_length=100)
    bunk_number = models.BigIntegerField(unique=True)
    reservation = models.CharField(max_length=100)  #need to make this a foreign key and have it reference a table with all members.

class Room(models.Model):
    room = models.CharField(max_length=100)


