from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations=True
    
    def create_user(self,email,password=None, **extra_fields):
        
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user must have is_staff true')
        
        return self.create_user(email,password,**extra_fields)




# adding spec and mobile fields into User model

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=30,null=True,blank=True)
    name=models.CharField(max_length=30,null=True,blank=True)
    
    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['password']
    def __str__(self):
        if self.is_superuser:
            return self.email +"("+" "+ "Admin" + " " +")"
        else:
            return  self.email +" "+"------->"+" "+self.first_name
        
