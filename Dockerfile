FROM python:3.12.2-bullseye

ENV PYTHONUNBUFFERED 1

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

# Copy entrypoint script
# I added this line to simplify the process of running the Django server for my challenge
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x ./sample_data/load_data.sh

# Run the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]