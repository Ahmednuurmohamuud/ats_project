from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True, null=True)
    education = models.TextField()
    experience = models.TextField()
    skills = models.CharField(max_length=300)
    cover_letter = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"
