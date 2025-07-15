# ats_project

**Final README Documentation (English)**

# ATS Project – Applicant Tracking System

This is a full-stack web application built using Django. The system is designed to help companies manage job postings and applicant submissions through a clean, user-friendly interface.

---

## 🏢 Features

### Admin Dashboard

* Simulated login (simple session-based)
* Create, edit, and delete job postings
* View all jobs
* View list of applicants per job
* View full CV information of each applicant
* Visual chart showing number of applicants per job (Chart.js)

### Public Application Form

* Input-only form (no file upload)
* Fields: Full Name, Email, Phone, LinkedIn, Education, Experience, Skills, Cover Letter, Position Applied For
* Responsive design with modern UI (Tailwind CSS + Animate.css)
* Confirmation and email notification on successful submission

### Email Notifications

* Applicant receives email confirming application
* Admin receives notification when a new application is submitted

---

## ⚡ Technologies Used

* Python & Django
* HTML5, Tailwind CSS, Animate.css
* Chart.js (for job statistics)
* SQLite (default Django database)

---

## 🚧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Ahmednuurmohamuud/ats_project.git
cd ats_project
```

2. **Create virtual environment & install dependencies**

```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Configure email in settings.py**

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'  halkan email so gali
EMAIL_HOST_PASSWORD = 'your_app_password' hlkan password email or app password  gasho
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'
```

4. **Run the server**

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🎥 Demo Video

\[Include your Loom or Google Drive video link here]

---




## 📊 Submission Info

* GitHub: [https://github.com/Ahmednuurmohamuud/ats\_project](https://github.com/Ahmednuurmohamuud/ats_project)
* Demo Video: \[Insert Link Here]
* Submit to: [info.hr@mizanhrconsulting.com](mailto:info.hr@mizanhrconsulting.com)
* Subject: Full Stack ATS Exam Submission – Ahmednuur Mohamuud Warsame

---

## ✅ Final Checklist Before Submission

* [x] Admin login implemented
* [x] Job CRUD (create/edit/delete) working
* [x] Applicant form fully functional
* [x] Email notifications working
* [x] Template design responsive + animated
* [x] GitHub repo ready
* [x] Demo video recorded
* [x] This documentation is completed

---


