from django.db import models
from user.models import user

class appointment_model(models.Model):
    appointment_id=models.AutoField(primary_key=True)
    # Related name must be a valid Python identifier or end with a '+'
    user_id1=models.ForeignKey(user,related_name="from+", on_delete=models.CASCADE)#student
    user_id2=models.ForeignKey(user, related_name="to+",on_delete=models.CASCADE)#prof
    date=models.DateField()
    time=models.TimeField()
    reason=models.TextField()
    status=models.IntegerField(default=0)#0 fro requested ,1 for accepted ,2 for rejected


    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.appointment_id)
