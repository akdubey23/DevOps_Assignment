# ACEest Fitness & Gym – DevOps Assignment

Flask web application with DevOps setup: tests, Docker, GitHub Actions CI, and Jenkins pipeline.

## Project Structure

```
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── test_app.py         # Unit tests (pytest)
├── Dockerfile          # Docker image
├── Jenkinsfile         # Jenkins pipeline
├── README.md
└── .github/workflows/
    └── ci.yml          # GitHub Actions CI
```

## Prerequisites

- Python 3.11
- pip
- Docker (for container builds)

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Visit: http://localhost:5000

## API Endpoints

| Endpoint  | Method | Description              |
|-----------|--------|--------------------------|
| `/`       | GET    | Welcome message          |
| `/health` | GET    | Health check             |
| `/version`| GET    | App version info         |

## Run tests

```bash
pytest test_app.py -v
```

## Docker

```bash
docker build -t flask-app:latest .
docker run -p 5000:5000 flask-app:latest
```

## GitHub Actions

CI runs on push/PR to `main` or `master`: installs deps → runs pytest → builds Docker image.

## Jenkins

Pipeline stages: Checkout → Install Dependencies → Run Tests → Build Docker Image.

---

Created for BITS Pilani DevOps Assignment.
