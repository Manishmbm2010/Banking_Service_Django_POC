# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6.4

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /home_banking_service

# Set the working directory to /music_service
WORKDIR /home_banking_service

# Copy the current directory contents into the container at /music_service
ADD . /home_banking_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate
ENV DJANGO_DB_NAME=default
ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin@gmail.com
ENV DJANGO_SU_PASSWORD=password123
ENV DJANGO_SETTINGS_MODULE=bankingSystem.settings
RUN python -c "import django,os; os.environ.setdefault(DJANGO_SETTINGS_MODULE, '$DJANGO_SETTINGS_MODULE'); django.setup(); \
   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
   get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
   username='$DJANGO_SU_NAME', \
   email='$DJANGO_SU_EMAIL', \
   password='$DJANGO_SU_PASSWORD')"
