from django.urls import path
from . import views

urlpatterns = [
    # ex: /backend/
    path("", views.index, name="index"),
    # Get a user
    # ex: /backend/tommy/
    path("<name>/", views.user, name = "user"),
    # List all user applications
    # ex: /backend/tommy/applications/
    path("<name>/applications", views.user_applications, name = "applications"),
    # Get a specific application
    # ex: /backend/tommy/applications/5 the 5th application a user ever made
    path("<name>/applications/<int:application_id>", views.user_application, name = "applications"),
    # Lists all jobs available
    # ex: /backend/jobs/
    path("jobs/", views.jobs, name = "jobs"),
    # Get a specific job posting
    # ex: /backend/jobs/5
    path("jobs/<int:job_id>/", views.job, name = "job"),
    path("jobs/<int:job_id>/apply/<name>", views.apply_to_job, name = "apply")
]
