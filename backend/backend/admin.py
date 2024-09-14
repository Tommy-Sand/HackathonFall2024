from django.contrib import admin
from .models import User, Job, JobApplication

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'position') 
   

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job_posting', 'send_date', 'status')


admin.site.register(User, UserAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)