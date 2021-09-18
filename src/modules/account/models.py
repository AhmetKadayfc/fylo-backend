from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)


#Override UserManager class
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None, **other_fields):
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(email=self.normalize_email(email),
                          username=username, first_name=first_name, last_name=last_name, **other_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        user = self.create_user(
            username=username, email=email, first_name=None, last_name=None, password=password, **other_fields)

        return user


#Override User model
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/users',null=True, blank=True)

    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
