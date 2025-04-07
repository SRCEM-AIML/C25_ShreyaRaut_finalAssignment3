# My Flask + Django Web Apps with Docker Compose

This project demonstrates how to build and run two web applications — one using Flask and the other using Django — managed together with Docker Compose.

## Project Overview
The repository contains:

- A Flask application with a simple homepage.
- A Django application featuring an item listing, admin panel, and a form to add new items.
- Dockerfiles for both applications.
- A Docker Compose configuration to orchestrate the apps.

## Directory Structure
```
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
```

## How to Run the Project

### Prerequisites
- Ensure Docker and Docker Compose are installed and running on your system.

### Steps to Run
1. Build and start the containers:
   ```
   docker-compose up --build
   ```
2. Access the applications in your browser:
   - Flask App: `http://localhost:5000`
   - Django App: `http://localhost:8000`

## App Details

### 🔷 Flask App
- A simple Python Flask application (`app.py`).
- Displays a basic homepage message.
- Runs on port `5000`.
- Dockerized with its own `Dockerfile`.

### 🟦 Django App
- A standard Django project (`myproject`) with an app called `itemlist`.
- Features:
  - Item list view.
  - Form to add new items.
  - Admin panel at `/admin`.
- Runs on port `8000`.
- Database: SQLite.

## Docker Hub Images
If you prefer not to build locally, you can pull pre-built images from Docker Hub:

- Flask App:
  ```
[  docker pull <shreyaraut12>/my-flask-app](https://hub.docker.com/repository/docker/shreyaraut12/flask_app/general)
  ```
- Django App:
  ```
  [docker pull <shreyaraut12>/my-django-app](https://hub.docker.com/r/shreyaraut12/django_app)
  ```

## Notes
- To apply migrations for the Django app:
  ```
  docker exec -it myproject-djangoapp-1 python manage.py migrate
  ```
- Access the Django admin panel:
  - Go to `http://localhost:8000/admin`.
  - Create a superuser:
    ```
    docker exec -it myproject-djangoapp-1 python manage.py createsuperuser
    ```

## Author
- **Name:** Shreya Raut
- **GitHub:** github.com/Shreyaraut12
- **Docker Hub:** hub.docker.com/u/shreyaraut12


