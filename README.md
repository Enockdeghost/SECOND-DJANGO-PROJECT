# Simple Django Login and Registration System

A lightweight authentication system built with Django, featuring user registration, login, and logout functionality. The frontend is styled with Bootstrap 5 using a clean two-color theme (blue and light gray).

## Features

- User registration with Django's built-in `UserCreationForm`
- User login using Django's `LoginView`
- User logout using Django's `LogoutView` (POST only for security)
- Bootstrap 5 styled templates with a responsive design
- Customizable two-color scheme (easily change colors in `base.html`)
- Messages framework for user feedback (e.g., success on registration)
- Home page accessible only to authenticated users

## Requirements

- Python 3.8+
- Django 4.x

## Installation

auth_project/
├── auth_project/          # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/              # Main app
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── registration/
│   │       ├── login.html
│   │       └── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md
