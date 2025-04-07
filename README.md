My Flask + Django Web Apps with Docker Compose
This project demonstrates how to build and run two web applications — one using Flask and the other using Django — managed together with Docker Compose.

Project Overview
The repository contains:

A Flask application with a simple homepage.
A Django application featuring an item listing, admin panel, and a form to add new items.
Dockerfiles for both applications.
A Docker Compose configuration to orchestrate the apps.
Directory Structure
text

Collapse

Wrap

Copy
myproject/
├── flask_app/
│   ├── app.py
│   └── Dockerfile
│
├── django_app/
│   ├── Dockerfile
│   ├── manage.py
│   ├── myproject/
│   └── itemlist/
│
├── docker-compose.yml
└── README.md
How to Run the Project
Prerequisites
Ensure Docker and Docker Compose are installed and running on your system.
Steps to Run
Build and start the containers:
text

Collapse

Wrap

Copy
docker-compose up --build
Access the applications in your browser:
Flask App: http://localhost:5000
Django App: http://localhost:8000
App Details
🔷 Flask App
A simple Python Flask application (app.py).
Displays a basic homepage message.
Runs on port 5000.
Dockerized with its own Dockerfile.
🟦 Django App
A standard Django project (myproject) with an app called itemlist.
Features:
Item list view.
Form to add new items.
Admin panel at /admin.
Runs on port 8000.
Database: SQLite.
Docker Hub Images
If you prefer not to build locally, you can pull pre-built images from Docker Hub:

Flask App:
text

Collapse

Wrap

Copy
docker pull shreyaraut12/my-flask-app
(See: https://hub.docker.com/r/shreyaraut12/my-flask-app)
Django App:
text

Collapse

Wrap

Copy
docker pull shreyaraut12/my-django-app
(See: https://hub.docker.com/r/shreyaraut12/my-django-app)
Notes
To apply migrations for the Django app:
text

Collapse

Wrap

Copy
docker exec -it myproject-djangoapp-1 python manage.py migrate
Access the Django admin panel:
Go to http://localhost:8000/admin.
Create a superuser:
text

Collapse

Wrap

Copy
docker exec -it myproject-djangoapp-1 python manage.py createsuperuser
Author
Name: Shreya Raut
GitHub: github.com/Shreyaraut12
Docker Hub: hub.docker.com/u/shreyaraut12
