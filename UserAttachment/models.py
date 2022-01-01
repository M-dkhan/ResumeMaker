from django.db import models
import uuid 
from CustomUser.models import CustomUser 

# Create your models here.
class WorkExperince(models.Model):
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    employer = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date =  models.DateField()
    description = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.id)


class Education(models.Model):
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    institution_name = models.CharField(max_length=200)
    start_date = models.DateField() 
    end_date = models.DateField()
    description = models.TextField()    
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.id)

class language(models.Model):
    LEVEL = (
        ('native', 'Native'),
        ('professional', 'Professional'),
        ('medium', 'Good Working Knowledge'),
    )
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=200, choices=LEVEL)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    

    def __str__(self):
        return str(self.id)

class skill(models.Model):
    LEVEL = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('skillfull', 'Skillfull'),
        ('experinced', 'Experinced'),
        ('expert', 'Expert'),
    )
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=200, choices=LEVEL)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    

    def __str__(self):
        return str(self.id)

class Intrest(models.Model):
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    hobby = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.id)

class Certification(models.Model):
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.id)


class Achivement(models.Model):
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.id)
    
class CustomSection(models.Model):
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.id)
    