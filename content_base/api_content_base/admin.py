from django.contrib import admin
from .models import course_list,tag
# Register your models here.
admin.site.register(course_list)
admin.site.register(tag)