FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/code

# Set work directory
WORKDIR /code

# Install system dependencies and uv
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install uv

# Copy requirements.txt
COPY requirements.txt /code/requirements.txt

RUN python -m uv pip install --system --requirement /code/requirements.txt

# Copy project
COPY . /code/

# Run migrations and collect static files
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Run the application; I'll want gunicorn or something different for prod
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
