from django.db import models
from user.models import user

class mess_model(models.Model):
    mess_id=models.AutoField(primary_key=True)

    name=models.CharField(max_length=264)
    hostel=models.CharField(max_length=264)
    breakfast=models.TextField(blank=True,null=True)
    lunch=models.TextField(blank=True,null=True)
    dinner=models.TextField(blank=True,null=True)
    breakfast2=models.TextField(blank=True,null=True)
    lunch2=models.TextField(blank=True,null=True)
    dinner2=models.TextField(blank=True,null=True)
    contact=models.IntegerField(null=True,blank=True)

    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.mess_id)




class cancel_model(models.Model):
    cancel_id=models.AutoField(primary_key=True)
    # Related name must be a valid Python identifier or end with a '+'
    user_id=models.ForeignKey(user, on_delete=models.CASCADE)#student
    mess_id=models.ForeignKey(mess_model,on_delete=models.CASCADE)#prof
    startdate=models.DateField(default='2001-12-09')
    starttime=models.IntegerField()#1 for brekfast 2for lunnch 3 for dinner
    enddate=models.DateField(default='2001-12-09')
    endtime=models.IntegerField()#1 for brekfast 2for lunnch 3 for dinner

    status=models.IntegerField(default=0)#0 fro requested ,1 for accepted ,2 for rejected


    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.cancel_id)
