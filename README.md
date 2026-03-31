# Todo App — DevOps & MLOps Assignment

| | |
|---|---|
| **Submitted by** | Anshika Gupta (0201AI221013) |
| **Semester** | 8th Sem |
| **Department** | Artificial Intelligence and Data Science |
| **Submitted to** | Prof. Praveen Patel |

---

## Assignment Brief

> Create a small web app and apply the following:
> 1. Dockerize it
> 2. Push code to GitHub
> 3. Configure GitHub Actions:
>    - On push → Run tests
>    - Build Docker image
>    - Deploy locally

---

## Tech Stack

- **Backend** — Django 5 + Gunicorn
- **Database** — SQLite (persisted via Docker volume)
- **Styling** — Tailwind CSS (CDN)
- **Container** — Docker + Docker Compose
- **CI/CD** — GitHub Actions

---

## Run Locally with Docker

```bash
git clone https://github.com/<your-username>/todo-app.git
cd todo-app
docker compose up --build
```

Open [http://localhost:8000](http://localhost:8000)

> Data persists in a Docker named volume (`db_data`). Survives container restarts.

---

## Run Without Docker

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Run Tests

```bash
python manage.py test tasks --verbosity=2
```

Tests cover:
- Model creation and toggle
- GET index page
- POST add task (valid + empty input)
- Toggle done status
- Delete task

---

## Project Structure

```
todo-app/
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # GitHub Actions pipeline
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── migrations/
│   └── templates/tasks/
│       └── index.html
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
└── manage.py
```

---

## CI/CD Pipeline (GitHub Actions)

Triggered on every push or pull request to `main`.

```
push to main
    │
    ▼
┌─────────┐     ┌───────────────────┐     ┌────────────────┐
│  Tests  │────▶│  Build Docker img │────▶│ Deploy Locally │
└─────────┘     └───────────────────┘     └────────────────┘
```

| Job | What it does |
|-----|-------------|
| **test** | Installs deps, runs Django test suite |
| **build** | Builds Docker image, saves as artifact |
| **deploy-local** | Loads image, runs `docker compose up`, health checks `localhost:8000` |

Each job only runs if the previous one passes.

---

## Push to GitHub

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/<your-username>/todo-app.git
git push -u origin main
```

The Actions pipeline will trigger automatically.
