from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Job, Applicant

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('deadline',)


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'job', 'submitted_at')
    search_fields = ('full_name', 'email', 'skills')
    list_filter = ('job',)
