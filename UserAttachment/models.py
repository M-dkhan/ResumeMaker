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
        return self.id


class Education(mdoels.Model):
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
        return self.id