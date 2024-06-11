#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput 
    --username $DJANGO_SUPERUSER_USERNAME
    --email $DJANGO_SUPERUSER_EMAIL
fi

# Start the Django development server
echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000