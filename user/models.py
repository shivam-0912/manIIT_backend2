from django.db import models

##Below are basically sql tables kinda things
# Create your models here.
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    usertype=models.IntegerField()#0 for student 1 for prof
    username=models.CharField(max_length=264)
    email_id=models.CharField(max_length=264,unique=True)
    password=models.CharField(max_length=264)
    activation=models.BooleanField(default=False)
    role=models.CharField(max_length=264,blank=True,null=True)#cr n ol
    authoritystatus=models.IntegerField(default=0)#0 for nothing 1 for pending 2 for accepted
    auth_name=models.CharField(max_length=264,blank=True,null=True)#club name
    department=models.CharField(max_length=264,blank=True,null=True)#1 for cse nd so on
    mess_id=models.IntegerField(blank=True,null=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True,null=True)#for uploading pictures to media/profile_pics folder


    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.user_id)

class authority(models.Model):
    authority_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    email_id=models.CharField(max_length=264)
    role=models.CharField(max_length=264,blank=True)

    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.authority_id)

