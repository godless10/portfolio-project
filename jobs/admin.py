from django.contrib import admin

# to show the model Job in the admin page
from .models import Job

admin.site.register(Job)
