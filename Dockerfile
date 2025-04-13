# Use official Python 3.12 as base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]