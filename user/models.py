from django.db import models

##Below are basically sql tables kinda things
# Create your models here.
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    email_id=models.CharField(max_length=264,unique=True)
    password=models.CharField(max_length=264)
    activation=models.BooleanField(default=False)
    role=models.CharField(max_length=264,blank=True)
    authoritystatus=models.IntegerField(default=0)
    auth_name=models.CharField(max_length=264,blank=True)
    department=models.CharField(max_length=264,blank=True)
    mess=models.CharField(max_length=264,blank=True)
 
    
    
    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.user_id)

class authority(models.Model):
    authority_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    email_id=models.CharField(max_length=264)
    role=models.CharField(max_length=264,blank=True)
    
    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.authority_id) 
    
