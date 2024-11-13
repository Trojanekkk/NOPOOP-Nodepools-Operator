FROM python:3.12-alpine

# Copy the requirements.txt file into the container
COPY requirements.txt /tmp

# Install the dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Set the working directory
WORKDIR /app

# Copy the app directory contents into the container at /app
COPY app /app

# Run the operator
CMD ["python", "main.py"]