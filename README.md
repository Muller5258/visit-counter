# visit-counter

A small FastAPI app that counts visits and stores them in PostgreSQL. Built to practice containerizing an app and shipping it through a full CI/CD pipeline.

## Endpoints

| Endpoint | Returns |
| --- | --- |
| `/` | Records a visit and returns the total count |
| `/health` | Health check |

## Docker

- **Multi-stage build:** dependencies are installed in a builder stage; only the installed packages and the code are copied into a clean final image.
- **Layer caching:** `requirements.txt` is copied and installed before the code, so code changes don't trigger a full reinstall.
- **Non-root user:** the app runs as `appuser`.
- **12-factor config:** the database URL comes from an environment variable.

## Pipeline

1. Push to `main`
2. GitHub Actions builds the image and pushes it to `ghcr.io/muller5258/visit-counter`
3. The home server pulls the new image within 5 minutes and replaces the container
4. Visit data persists across deployments in a Docker volume

The server side lives in my [homelab](https://github.com/Muller5258/homelab) repo.

## Run locally

    docker compose up --build

Then open http://localhost:8000
