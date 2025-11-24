# 🚀 TalentHub – Full-Stack Recruitment System

TalentHub is a full-stack web app that connects candidates with recruiters. Candidates can browse and apply to jobs, while recruiters can post openings and manage applications. Built using Django with secure role-based access and a responsive UI.

## ✨ Features
### 🔐 Dual-Role Authentication
- Separate login & signup for Candidates and Recruiters  
- Role-based dashboards  
- Ownership-protected actions  

### 🏢 Recruiter Dashboard
- Create, edit, delete job posts  
- View and manage all applicant details  

### 👤 Candidate Dashboard
- Browse and apply to jobs  
- One-click apply  
- Track application status  

### 📌 Job Management
- Full CRUD on job listings  
- Only owners can modify their postings  

### 📊 Status Tracking
Application workflow: **Applied → Under Review → Shortlisted → Hired**

### 🛡️ Role-Based Security (RBAC)
- Custom Django decorators for secure routes  
- Isolated recruiter/candidate operations  

### 💻 Responsive UI
- Bootstrap 5  
- Clean and mobile-friendly layout  
- Crispy Forms for smooth form handling  

## 🧰 Tech Stack
**Frontend:** HTML5, CSS3, JS, Bootstrap 5  
**Backend:** Django, DTL, Python  
**Database:** SQLite  
**Forms:** Django Crispy Forms

## 📦 Setup Instructions
```bash
git clone https://github.com/Abhay-singh26124/TalentHub.git
cd TalentHub
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
