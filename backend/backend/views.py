from django.shortcuts import render

from .models import User

from django.http import HttpResponse, HttpResponseBadRequest

def index(request):
    return HttpResponse("Is this setup properly?")

def create_user(request, new_name):
    if User.objects.filter(name=new_name).count() == 0:
        new_user = User.objects.create(name=new_name, resume=request.read())
        new_user.save()
        return HttpResponse("Successfully added {}".format(new_name))
    else:
        return HttpResponseBadRequest("User {} already exists".format(new_name))

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
