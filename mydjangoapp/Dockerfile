# Use the official Python image as the base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Poetry
RUN pip install poetry

# Set Poetry configuration
RUN poetry config virtualenvs.in-project false \
    && poetry config virtualenvs.create false

# Set the working directory
WORKDIR /app

# Copy the Poetry files and install dependencies
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

# Copy the Django application code
COPY . /app/

# Expose the port on which the Django app will run
EXPOSE 8000

# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
