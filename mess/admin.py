from django.contrib import admin
from mess.models import mess_model,cancel_model
# Register your models here.
admin.site.register(mess_model)
admin.site.register(cancel_model)
