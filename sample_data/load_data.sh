#!/bin/bash

echo "Creating testing data..."
python manage.py loaddata /app/sample_data/Person.json
python manage.py loaddata /app/sample_data/Brand.json
python manage.py loaddata /app/sample_data/Color.json
python manage.py loaddata /app/sample_data/Vehicle.json
python manage.py loaddata /app/sample_data/Officer.json
python manage.py loaddata /app/sample_data/Group.json
python manage.py loaddata /app/sample_data/OfficerGroups.json
python manage.py loaddata /app/sample_data/Infractions.json
python manage.py user_set_default_password
