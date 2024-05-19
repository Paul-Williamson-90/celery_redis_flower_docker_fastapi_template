# Project Template Start for Celery, Redis, Flower, Docker and Fast-API

# What is it for?
- A quick start project template for creating an application where the BE container is separate from the endpoints/frontend.
- The connection between the BE and FE/Endpoints is handled by Celery workers, using a Redis broker and Flower for inspecting and monitoring celery tasks.
- When an endpoint is triggered, a celery worker is spawned to handle the BE processing, this enables asychronoous processing in the BE and avoids deadlocks in the FE/endpoints from waiting for the BE to complete a task.

# How to run?
- From the root dir:
    - Ensure Docker Desktop is running
    - Run in the CLI:
        - docker-compose up --build

# How to test
- See the examples in demo.ipynb