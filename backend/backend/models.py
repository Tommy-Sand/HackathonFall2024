from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    resume = models.TextField()

class Job(models.Model):
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(Job, on_delete=models.PROTECT)
    send_date = models.DateTimeField("date sent")
    status = models.CharField(max_length=200)
    interview_date = models.DateTimeField("date interview")
    accept_date = models.DateTimeField("date accept")
    resume = models.TextField()
