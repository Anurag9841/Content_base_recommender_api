from django.db import models

class course_list(models.Model):
    id = models.IntegerField(primary_key=True)
    Course_Name = models.CharField(max_length=100, blank= True,null=True)
    course_code = models.CharField(max_length=100, blank= True,null=True)
    Course_Description = models.CharField(max_length=100, blank= True,null=True)
    Course_Cover_File = models.CharField(max_length=100, blank= True,null=True)
    Course_Level = models.IntegerField(null=True,blank=True)
    Course_Info = models.CharField(max_length=100, blank= True,null=True)
    Use_Flag = models.BooleanField(null=True,blank=True)
    Register_DateTime = models.CharField(max_length=100, blank= True,null=True)
    Updated_DateTime = models.CharField(max_length=100, blank= True,null=True)
    Register_Agent = models.CharField(max_length=100, blank= True,null=True)
    Course_Provider = models.CharField(max_length=100, blank= True,null=True)
    Syllabus = models.CharField(max_length=100, blank= True,null=True)
    keyword = models.CharField(max_length=100, blank= True,null=True)
    Center_Code = models.IntegerField(null=True,blank=True)
    tag = models.CharField(max_length=100, blank= True,null=True)

class tag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=100, blank= True,null=True)
    created_at = models.CharField(max_length=100, blank= True,null=True)
    updated_at = models.CharField(max_length=100, blank= True,null=True)




# Create your models here.
