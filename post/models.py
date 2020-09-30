from django.db import models
from user.models import user
from club.models import club
# Create your models here.
class user_post(models.Model):
    user_post_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(user, on_delete=models.CASCADE)
 
    post_type=models.BooleanField(default=False)#0 for event 1 for post
    title=models.CharField(max_length=264)
    image=models.ImageField(upload_to='postmain',blank=True)
    description=models.TextField()
    location=models.CharField(max_length=264)
    attachment=models.FileField(upload_to='postextra',blank=True)
    start=models.DateField()
    end=models.DateField()
    allin=models.IntegerField(default=0)#0 for no 1 for only students 2 for only prof 3 for both
   
    cse=models.IntegerField(default=0)#0 for no 1 for only students 2 for only prof 3 for both
    mnc=models.IntegerField(default=0)
    trical=models.IntegerField(default=0)
    tronix=models.IntegerField(default=0)
    civil=models.IntegerField(default=0)
    mst=models.IntegerField(default=0)
    cera=models.IntegerField(default=0)
    meta=models.IntegerField(default=0)
    mining=models.IntegerField(default=0)
    
    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.user_post_id)
    
    
class club_post(models.Model):
    club_post_id=models.AutoField(primary_key=True)
    club_id=models.ForeignKey(club, on_delete=models.CASCADE)
 
    post_type=models.BooleanField(default=False)#0 for event 1 for post
    title=models.CharField(max_length=264)
    image=models.URLField(max_length=264,blank=True)
    description=models.TextField()
    location=models.CharField(max_length=264)
    start=models.DateTimeField()
    end=models.DateTimeField()
    allin=models.IntegerField(default=0)#0 for no 1 for only students 2 for only prof 3 for both
    cse=models.IntegerField(default=0)
    mnc=models.IntegerField(default=0)
    trical=models.IntegerField(default=0)
    tronix=models.IntegerField(default=0)
    civil=models.IntegerField(default=0)
    mst=models.IntegerField(default=0)
    cera=models.IntegerField(default=0)
    meta=models.IntegerField(default=0)
    mining=models.IntegerField(default=0)
    
    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.club_post_id)
    
    