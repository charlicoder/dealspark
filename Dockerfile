# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    libssl-dev \
    && apt-get clean

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip && pip install httpx
RUN pip install -r requirements.txt


# Copy the entire Django project to the container
COPY . /app/

COPY entrypoint_prod.sh /app/

# Grant execute permissions to the entrypoint script
RUN chmod +x /app/entrypoint_prod.sh

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Set the entrypoint script as the container entrypoint
ENTRYPOINT ["/app/entrypoint_prod.sh"]
