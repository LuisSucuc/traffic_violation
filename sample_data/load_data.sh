#!/bin/bash

echo "Creating testing data..."
python manage.py loaddata /app/sample_data/Person.json
python manage.py loaddata /app/sample_data/Brand.json
python manage.py loaddata /app/sample_data/Color.json
python manage.py loaddata /app/sample_data/Vehicle.json
