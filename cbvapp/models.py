from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    username = models.CharField(max_length=200, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False)
    bio = models.TextField(null=True)
    social_handle = models.CharField(max_length=200, null=True)
    Otp_Validation=models.BooleanField(default=False )
    
    # avatar = CloudinaryField('image', null= True, default="avatar.svg")
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email 

class Priority(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Priority_Name = models.CharField(max_length=200, default="Default", unique=True, null=False, blank=False)
    cat_status=models.BooleanField(default=False )
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering =['-created']

    def __str__(self):
        return self.Priority_Name
    
class Colors(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Color_Name = models.CharField(max_length=200, default="Default", unique=True, null=False, blank=False)
    cat_status=models.BooleanField(default=False )
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering =['-created']

    def __str__(self):
        return self.Color_Name



class Note(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    Note_Priority =  models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    Note_Color = models.ForeignKey(Colors, on_delete=models.SET_NULL, null=True)
    Note_Title = models.CharField(max_length=200, null=False, blank=False)
    Description = models.TextField(null=False, blank=False)
    Note_Count = models.IntegerField(default=0)
    Reminder_Date = models.DateTimeField()
    Pinned_Note=models.BooleanField(default=False )
    Favourite_Note=models.BooleanField(default=False )
    post_status=models.BooleanField(default=False )
    # post_img = CloudinaryField('image', null=True, default="avatar.svg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =[ '-created']


    def __str__(self):
        return self.Note_Title