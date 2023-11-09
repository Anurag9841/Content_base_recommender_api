from django.contrib import admin
from .models import course_list,tag,preprocessedtag,preprocessedcourse
# Register your models here.
admin.site.register(course_list)
admin.site.register(tag)
admin.site.register(preprocessedtag)
admin.site.register(preprocessedcourse)

