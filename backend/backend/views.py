from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Is this setup properly?")

def user(request, name):
    return HttpResponse("/backend/<name> unimplemented")

def user_applications(request, name):
    return HttpResponse("/backend/<name>/applications unimplemented")

def user_application(request, name, application_id):
    return HttpResponse("/backend/<name>/applications/<int:application_id> unimplemented")

def jobs(request):
    return HttpResponse("/backend/jobs/ unimplemented")

def job(request, job_id):
    return HttpResponse("/backend/jobs/<int:job_id>/ unimplemented")

def apply_to_job(request, name, job_id):
    return HttpResponse("jobs/<int:job_id>/apply/<name> unimplemented")
