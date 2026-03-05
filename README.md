# Hello World App

A minimal HTTP server built with Python + FastAPI that exposes a Hello World endpoint.

## Language / Runtime

- **Language:** Python 3.12
- **Framework:** FastAPI + Uvicorn

## Endpoints

| Method | Path | Response |
|--------|------|----------|
| GET | `/` | `{"message": "Hello World"}` |
| GET | `/hello` | `{"message": "Hello World"}` |
| GET | `/health` | `{"status": "ok"}` |

## Run Locally (without Docker)

```bash
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

pip install -r requirements.txt
python app.py
# Server starts on http://localhost:9000
```

Test it:
```bash
curl http://localhost:9000/hello
# {"message":"Hello World"}
```

## Build the Docker Image

```bash
docker build -t hello-world-app .
```

## Run the Container Locally

```bash
docker run -p 9000:9000 hello-world-app
```

Test it:
```bash
curl http://localhost:9000/hello
# {"message":"Hello World"}
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `9000` | Port the server listens on |

## CI/CD

On every push to `main`, GitHub Actions:
1. Builds the Docker image
2. Pushes it to Amazon ECR with two tags: `latest` and the commit SHA
3. Updates the image tag in the deployments repo
4. ArgoCD detects the change and rolls out the new version