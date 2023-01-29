from django.contrib import admin
# from home.models import Contact or
from .models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Feedback)
admin.site.register(Information)
