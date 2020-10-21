from django.db import models

class canteen_model(models.Model):
    canteen_id=models.AutoField(primary_key=True)
    contact=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=264)
    # image=models.ImageField(upload_to='c',blank=True)
    # description=models.TextField()
    location=models.CharField(max_length=264,blank=True,null=True)
    items=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=264,blank=True,null=True)

    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.canteen_id)
