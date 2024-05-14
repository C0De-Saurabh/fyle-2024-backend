# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable for Windows PowerShell
ENV FLASK_APP="core/server.py"

# Run database migration
RUN flask db upgrade -d core/migrations/

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
