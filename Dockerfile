# Use the official Python image from the Docker Hub
FROM python:3.11

# Base image
FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.5.1
ENV PATH="${PATH}:/root/.local/bin"

# Working directory
WORKDIR /python_twitter

# System dependencies and Poetry installation (single RUN for better caching)
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="/root/.local/bin:$PATH"

# Install project dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Start the application
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
