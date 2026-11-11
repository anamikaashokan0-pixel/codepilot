from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_CHOICES = [

        ('student','student'),
        ('admin','admin')

    ]

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default="student")

    phone = models.CharField(max_length=20,unique=True)

    def __str__(self):

        return self.username
    


class StudentProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    profile_picture = models.ImageField(upload_to="profiles/",blank=True,null=True)

    bio = models.TextField(blank=True)

    institute = models.CharField(max_length=150,blank=True)

    qualification = models.CharField(max_length=100,blank=True)

    github_url = models.URLField(blank=True)

    linkedin_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


from django.db.models.signals import post_save

def create_student_profile(sender,instance,created,**kwargs): 

    if created and not instance.is_superuser:

        StudentProfile.objects.create(user=instance)

post_save.connect(create_student_profile,User)    








