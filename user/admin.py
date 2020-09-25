from django.contrib import admin

from user.models import user,authority
# Register your models here.
admin.site.register(user)
admin.site.register(authority)