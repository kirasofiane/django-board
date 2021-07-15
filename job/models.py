from django.db import models

# Create your models here.
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


class Job(models.Model):   #class equivalent to Table in db 
    title = models.CharField(max_length=100) # equvalent to colonn
    # location
    job_type = models.CharField(max_length=15, choices = JOB_TYPE)
    description = models.TextField(max_length=1000)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    def __str__(self):
        return self.title