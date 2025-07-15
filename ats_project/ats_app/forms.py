from django import forms
from .models import Job, Applicant

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'deadline']


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'full_name',
            'email',
            'phone',
            'linkedin',
            'education',
            'experience',
            'skills',
            'cover_letter'
        ]
        widgets = {
            'education': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Example:\n- Jazeera University, BSc Computer Science, 2023'}),
            'experience': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Example:\n- Google, Frontend Developer, 2 years'}),
            'cover_letter': forms.Textarea(attrs={'rows': 4}),
        }
     
     
