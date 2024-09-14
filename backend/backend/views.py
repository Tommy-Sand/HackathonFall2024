from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.dateparse import parse_datetime

from .models import User, JobApplication, Job

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

@csrf_exempt
def apply_to_job(request, name, job_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(name=name)
            job = Job.objects.get(id=job_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist."}, status=404)
        except Job.DoesNotExist:
            return JsonResponse({"error": "Job does not exist."}, status=404)


        try:
            data = json.loads(request.body)
            send_date = parse_datetime(data['send_date'])
            interview_date = parse_datetime(data.get('interview_date')) if data.get('interview_date') else None
            accept_date = parse_datetime(data.get('accept_date')) if data.get('accept_date') else None
            status = data['status']
            resume = data.get('resume', '')

            application = JobApplication.objects.create(
                user=user,
                job_posting=job,
                send_date=send_date,
                status=status,
                interview_date=interview_date,
                accept_date=accept_date,
                resume=resume
            )

        
            response_data = {
                "message": f"Applied to job {job_id} successfully.",
                "application": {
                    "id": application.id,
                    "user": application.user.name,
                    "job": application.job_posting.id,
                    "send_date": application.send_date.isoformat() if application.send_date else None,
                    "status": application.status,
                    "interview_date": application.interview_date.isoformat() if application.interview_date else None,
                    "accept_date": application.accept_date.isoformat() if application.accept_date else None,
                    "resume": application.resume
                }
            }
            return JsonResponse(response_data, status=201)

        except (ValueError, KeyError) as e:
            return JsonResponse({"error": "Invalid input data.", "details": str(e)}, status=400)


    return JsonResponse({"error": "Invalid request method"}, status=405)