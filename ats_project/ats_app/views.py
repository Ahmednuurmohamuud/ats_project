from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Job, Applicant
from .forms import JobForm, ApplicantForm
from django.contrib import messages

# Hardcoded login credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

# Public: Show list of jobs
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'job_list.html', {'jobs': jobs})


# Public: Apply to a job
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job = job   # <-- Halkaan ayaa muhiim ah
            applicant.save()

            # Email notification to applicant
            send_mail(
                subject=f'Thank you for applying for {job.title}',
                message=f'Dear {applicant.full_name},\n\nThank you for applying for the position "{job.title}". We will review your application and get back to you soon.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[applicant.email],
                fail_silently=False,
            )

            # Email notification to admin
            send_mail(
                subject=f'New application for {job.title}',
                message=f'You have received a new application from {applicant.full_name} ({applicant.email}) for the position "{job.title}".',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Admin email
                fail_silently=False,
            )

            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job_list')
    else:
        form = ApplicantForm()

    return render(request, 'apply_form.html', {'form': form, 'job': job})



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['admin_logged_in'] = True
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'admin_login.html')


# Logout view
def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')


# Admin dashboard: show job list
def dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    jobs = Job.objects.all().order_by('-created_at')
    job_count = jobs.count()
    applicant_count = Applicant.objects.count()

    chart_data = [{'title': job.title, 'count': job.applicant_set.count()} for job in jobs]

    return render(request, 'dashboard.html', {
        'jobs': jobs,
        'job_count': job_count,
        'applicant_count': applicant_count,
        'chart_data': chart_data
    })


# Create job (admin)
def create_job(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'create_job.html', {'form': form})


# Edit job
def edit_job(request, job_id):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form})


# Delete job
def delete_job(request, job_id):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return redirect('dashboard')


# List of applicants for a job
def applicant_list(request, job_id):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    job = get_object_or_404(Job, id=job_id)
    applicants = Applicant.objects.filter(job=job)
    return render(request, 'applicant_list.html', {'job': job, 'applicants': applicants})


# Applicant CV detail
def applicant_detail(request, applicant_id):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    applicant = get_object_or_404(Applicant, id=applicant_id)
    return render(request, 'applicant_detail.html', {'applicant': applicant})



