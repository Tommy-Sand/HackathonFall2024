from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    resume = models.TextField()

class Job(models.Model):
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()

class JobApplication(models.Model):
    APPLIED = "A"
    INTERVIEW = "I"
    OFFER = "O"
    REJECTION = "R"
    STATUS = (
        (APPLIED, "Applied"),
        (INTERVIEW, "Interview"),
        (OFFER, "Offer"),
        (REJECTION, "Rejection")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(Job, on_delete=models.PROTECT)
    send_date = models.DateTimeField("date sent")
    status = models.CharField(max_length=1, choices=STATUS, default=APPLIED)
    interview_date = models.DateTimeField("date interview", blank=True, null=True)
    accept_date = models.DateTimeField("date accept", blank=True, null=True)
    resume = models.TextField()
