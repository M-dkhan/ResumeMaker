from django.db import models
import uuid
# Create your models here.

class CustomUser(models.Model):
    MARITAL_STATUS_TYPE = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
    )
    GENDER_TYPE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    # user = 
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length= 200)
    country = models.CharField(max_length=200)
    dob = models.DateField(max_length=8)
    place_of_birth = models.CharField(max_length=200)
    marital_status = models.CharField(max_length=200, choices=MARITAL_STATUS_TYPE)
    gender = models.CharField(max_length=200, choices=GENDER_TYPE)
    nationality = models.CharField(max_length=200)
    github_link = models.CharField( max_length=500,blank=True,null=True)
    linked_in_link = models.CharField(max_length=500,blank=True, null=True)
    website_link = models.CharField(max_length=500, blank=True,null=True)
    resume_objective = models.TextField()


    def __str__(self):
        return self.first_name
