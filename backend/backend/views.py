from django.shortcuts import render

from .models import User, JobApplication

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

def index(request):
    return HttpResponse("Is this setup properly?")

def create_user(request, new_name):
    if User.objects.filter(name=new_name).count() == 0:
        new_user = User.objects.create(name=new_name, resume=request.read())
        new_user.save()
        return HttpResponse("Successfully added {}".format(new_name))
    return HttpResponseBadRequest("User {} already exists".format(new_name))

def user(request, name):
    user = User.objects.get(name=name)
    if user:
        json = dict()
        json["name"] = user.name
        json["applications"] = []
        for application in list(JobApplication.objects.filter(user=user)):
            application_json = dict()
            application_json["send_date"] = application.send_date
            application_json["status"] = application.status
            application_json["interview_date"] = application.interview_date
            application_json["accept_date"] = application.accept_date
            #Resume is not included since it isn't always needed
            #application_json["resume"] = application.resume
            json["applications"].append(application_json)
        return JsonResponse(json)
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
