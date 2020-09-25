from django.db import models

# Create your models here.
from user.models import user

class club(models.Model):
    club_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=264,blank=True)
    council=models.CharField(max_length=264,blank=True)
    email_id=models.CharField(max_length=264)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True)
    profile=models.URLField(blank=True)
    description=models.TextField(blank=True)
    phone=models.IntegerField(blank=True,null=True)
        
    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.club_id)