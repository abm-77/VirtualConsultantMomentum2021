# Use Python 3.7.2 image
FROM python:3.7.2-stretch

# Set Working Directory
WORKDIR /app 

# Copy the Current Directory Contents Into the Container at /app 
ADD . /app 

# Install Dependencies
RUN pip install -r requirements.txt

# Run the Command to Start uWSGI
CMD ["uwsgi", "app.ini"]
