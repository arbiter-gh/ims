# Project Title

Django Beginner Project - Internship at Ardent Computech Pvt. Ltd.

[//]: # (## Table of Contents)

[//]: # ()
[//]: # (- [Introduction]&#40;#introduction&#41;)

[//]: # (- [Features]&#40;#features&#41;)

[//]: # (- [Requirements]&#40;#requirements&#41;)

[//]: # (- [Installation]&#40;#installation&#41;)

[//]: # (- [Usage]&#40;#usage&#41;)

[//]: # (- [Project Structure]&#40;#project-structure&#41;)

[//]: # (- [Known Issues]&#40;#known-issues&#41;)

[//]: # (- [Contributing]&#40;#contributing&#41;)

[//]: # (- [License]&#40;#license&#41;)

[//]: # (- [Acknowledgements]&#40;#acknowledgements&#41;)

## Introduction

This project is a web application developed using Django during my internship at Ardent Computech Pvt. Ltd. It is one of my beginner projects, and while it demonstrates fundamental Django concepts and practices, it may contain errors and areas for improvement.

## Features

- User authentication (login, logout, registration)
- CRUD operations for a sample model (e.g., blog posts)
- Basic templates for rendering views
- Simple form handling
- Admin interface for managing models

## Requirements


- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/arbiter-gh/ims.git
   cd ims
   ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  Install the required packages:
    ```
    pip install -r requirements.txt
    ```

4.  Apply migrations to set up the database:
    ```
    python manage.py migrate
    
    ```
    
5. Create a superuser for the admin interface:
    ```
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```
    python manage.py runserver
    ```
Open your browser and go to http://127.0.0.1:8000 to see the application running.

## Known Issues

This project was a beginner-level attempt, so it may have some bugs and security issues.
Error handling is minimal and might not cover all edge cases.
The user interface is basic and could be improved with better styling and JavaScript functionality.
Optimization for larger datasets and performance tuning has not been done.

## Acknowledgements
Thanks to Ardent Computech Pvt. Ltd. for the opportunity to work on this project.
Special thanks to my mentors and colleagues for their support and guidance.
Django documentation for comprehensive guides and tutorials.