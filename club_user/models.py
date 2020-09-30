from django.db import models

from user.models import user
from club.models import club

class club_user_model(models.Model):
    club_user_id=models.AutoField(primary_key=True)
    club_id=models.ForeignKey(club,on_delete=models.CASCADE)
    
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    
        
    def __str__(self):#this is basically shorthand when we call the object so this will be retured
        return str(self.club_user_id)
