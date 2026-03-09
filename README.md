# ACEest Fitness & Gym – DevOps Assignment

**Course:** Introduction to DevOps (CSIZG514/SEZG514/SEUSZG514)  
**Assignment 1:** Implementing Automated CI/CD Pipelines for ACEest Fitness & Gym

A Flask web application for fitness and gym management, with automated CI/CD via GitHub Actions and Jenkins.

---

## Project Structure

```
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── test_app.py               # Pytest unit test suite
├── Dockerfile                # Container definition
├── Jenkinsfile               # Jenkins pipeline
├── README.md
└── .github/workflows/
    └── main.yml              # GitHub Actions CI/CD workflow
```

---

## 1. Local Setup and Execution

### Prerequisites

- Python 3.11 (or compatible)
- pip
- Docker (for containerization)

### Install and Run

```bash
# Clone the repository
git clone https://github.com/<your-username>/DevOps_Assignment.git
cd DevOps_Assignment

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The app will be available at **http://localhost:5000**

### API Endpoints

| Endpoint   | Method | Description        |
|------------|--------|--------------------|
| `/`        | GET    | Welcome message    |
| `/health`  | GET    | Health check       |
| `/version` | GET    | Application version |

---

## 2. Running Tests Manually

```bash
# Install dependencies first (if not already done)
pip install -r requirements.txt

# Run the Pytest suite
pytest test_app.py -v
```

For coverage:

```bash
pip install pytest-cov
pytest test_app.py -v --cov=app
```

---

## 3. Docker

### Build

```bash
docker build -t flask-app:latest .
```

### Run

```bash
docker run -p 5000:5000 flask-app:latest
```

### Run Tests Inside Container

```bash
docker run --rm flask-app:latest pytest test_app.py -v
```

---

## 4. Jenkins Integration

The Jenkins pipeline is defined in `Jenkinsfile`.

### Pipeline Stages

1. **Checkout** – Pull latest code from GitHub
2. **Install Dependencies** – Install Python packages from `requirements.txt`
3. **Run Tests** – Execute Pytest
4. **Build Docker Image** – Build the container with `docker build`

### Setup

1. Install Jenkins with Docker and Python available
2. Create a new **Pipeline** job
3. Connect to the GitHub repository
4. Choose "Pipeline script from SCM" and point to `Jenkinsfile`
5. Trigger a build (manually or via webhook)

---

## 5. GitHub Actions CI/CD Pipeline

The pipeline is defined in `.github/workflows/main.yml` and runs on every **push** and **pull_request** to `main` or `master`.

### Pipeline Stages

1. **Build & Lint** – Compile the application and check for syntax errors  
2. **Docker Image Assembly** – Build the Docker image  
3. **Automated Testing** – Run the Pytest suite inside the container to confirm stability  

### Workflow Overview

```
Push/PR → Checkout → Set up Python → Install deps → Build & Lint → Build Docker → Run Pytest in container
```

Pipeline status is visible in the **Actions** tab of the GitHub repository.

---

## Required Deliverables Checklist

- [x] **Source Code:** `app.py`, `requirements.txt`
- [x] **Test Suite:** Pytest script (`test_app.py`)
- [x] **Infrastructure as Code:** `Dockerfile`, `.github/workflows/main.yml`
- [x] **Documentation:** Local setup, manual test steps, Jenkins and GitHub Actions overview

---

*Created for BITS Pilani DevOps Assignment – ACEest Fitness & Gym*
