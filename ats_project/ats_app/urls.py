from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('jobs/create/', views.create_job, name='create_job'),
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit_job'),
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete_job'),
    path('jobs/<int:job_id>/applicants/', views.applicant_list, name='applicant_list'),
    path('applicants/<int:applicant_id>/', views.applicant_detail, name='applicant_detail'),
    path('logout/', views.admin_logout, name='logout'),
]
