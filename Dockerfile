FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies and uv
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://github.com/astral-sh/uv/releases/latest/download/uv-linux-x64 -o /usr/local/bin/uv \
    && chmod +x /usr/local/bin/uv

# Copy project files
COPY pyproject.toml .
COPY . .

# Install dependencies using uv
RUN uv pip install --system .

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Run the application; I'll want gunicorn or something different for prod
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
