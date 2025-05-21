# User Authentication System

A Django-based web application for user authentication, registration, and role-based dashboards.

## Project Overview

This application allows users to sign up and log in as different types of users (Patient or Doctor). Upon login, users are redirected to their respective dashboards displaying their profile information.

## Features

- **User Authentication**: Secure login/logout functionality
- **User Registration**: Comprehensive signup form with validation
- **User Types**: Support for different user types (Patient, Doctor)
- **Profile Management**: Profile picture upload and storage
- **Role-based Access**: Different dashboards for different user types
- **Responsive Design**: Bootstrap-based responsive interface

## Technical Details

### Technologies Used

- **Backend**: Python Django 5.2.1
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Image Storage**: Django's built-in file handling

### Project Structure

```
user_auth_system/
├── accounts/                    # Main application
│   ├── migrations/              # Database migrations
│   ├── admin.py                 # Admin configuration
│   ├── forms.py                 # Form definitions
│   ├── models.py                # Data models
│   ├── urls.py                  # URL configurations
│   └── views.py                 # View functions
├── media/                       # User-uploaded media
│   └── profile_pics/            # Profile pictures
├── static/                      # Static files
├── templates/                   # HTML templates
│   └── accounts/
│       ├── base.html            # Base template
│       ├── home.html            # Homepage template
│       ├── login.html           # Login page template
│       ├── logout.html          # Logout page template
│       ├── patient_dashboard.html # Patient dashboard template
│       ├── doctor_dashboard.html  # Doctor dashboard template
│       └── signup.html          # Registration page template
├── user_auth_system/            # Project configuration
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Project URLs
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django management script
└── README.md                    # Project documentation (this file)
```

## Setup and Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
   ```
   git clone <repository-url>
   cd user_auth_system
   ```

2. Install required dependencies:
   ```
   pip install django pillow
   ```

3. Apply migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at http://127.0.0.1:8000/

## User Guide

### Registration

1. Navigate to the Sign Up page
2. Fill in the required details:
   - First Name
   - Last Name
   - Username
   - Email
   - Profile Picture (optional)
   - User Type (Patient or Doctor)
   - Address information
   - Password (with confirmation)
3. Submit the form

### Login

1. Navigate to the Login page
2. Enter your username and password
3. Click "Login"

### Dashboard Access

After login, you'll be automatically redirected to the appropriate dashboard based on your user type:
- Patient Dashboard: http://127.0.0.1:8000/dashboard/patient/
- Doctor Dashboard: http://127.0.0.1:8000/dashboard/doctor/

### Logout

You can log out:
- Using the Logout button in the navigation bar
- Using the Logout buttons at the bottom of your dashboard

## Security Features

- Django's built-in authentication system
- Password validation and hashing
- CSRF protection for forms
- Secure logout mechanisms (using POST method)
- Role-based access control