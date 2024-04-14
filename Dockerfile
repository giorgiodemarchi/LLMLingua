# Use an official Python runtime as a parent image
FROM runpod/pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04

# Set the working directory in the container
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Clone the repository
ARG GIT_REPO="https://github.com/giorgiodemarchi/LLMLingua.git"
RUN git clone ${GIT_REPO} /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 8000

# Command to run the application
CMD [ "python", "-u", "/app.py" ]