# Specify our container base image
FROM python:3.9

# Select a working directory within our container
WORKDIR /usr/src/app

# Copy everything from our project root into our WORK DIRECTORY directory
COPY ./app/* .

# Install dependencies
RUN pip install -r requirements.txt

# Expose a port
EXPOSE 80

# Execute this command on start
ENTRYPOINT ["python", "./app.py"]
