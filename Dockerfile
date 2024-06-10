# Use a slim Python image to reduce size
FROM python:3.12.2-bullseye

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*
    
# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project code
COPY . .


# Make migrations and create superuser
#RUN python manage.py makemigrations
#RUN python manage.py migrate


# Expose port for Django (usually 8000)
EXPOSE 8000

# Run command to start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]