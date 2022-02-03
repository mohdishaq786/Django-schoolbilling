from django.contrib import admin
from user.models import userprofile
from user.models import contact


# Register your models here.
admin.site.register(userprofile)
admin.site.register(contact)