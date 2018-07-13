## Project :  Home Banking System as a Service

Code provide "Home Banking solution" as a service that runs in a docker container.

## Project Brief

There are total 3 services/entites

1. Customer service will let you perform create/retrieve/update & delete customer 
2. Account service will let you perform create/retrieve/update & delete customer's account
3. Credit Tranfer service will let you perform initiate payments and retrieve/update/delete existing payments
 
## Technology stack

1. Django Rest Framework for writing Rest API
2. PyCharm for code development
3. In build sqllite database for storing data
4. pip for dependency management	
5. Docker for containring the solution


### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment notes on how to deploy the project in your system

### Prerequisites

Docker machine should be up and running. Docker compose should be installed

### Run Test Cases(Total 16 test cases)

1. In Conatiner

* git clone https://Manishmbm2010@bitbucket.org/Manishmbm2010/home_banking_service_django_poc.git
* cd home_banking_service_django_poc/
* sudo docker-compose  -f docker-compose-test.yml up --build

2. Without Conatiner

* git clone https://Manishmbm2010@bitbucket.org/Manishmbm2010/home_banking_service_django_poc.git
* cd home_banking_service_django_poc/
* pip install -r requirements.txt
* python manage.py makemigrations customer
* python manage.py makemigrations account
* python manage.py makemigrations payments 
* python manage.py migrate
* python manage.py test

#### during manually testing , if test has to be rerun again ,please execute below steps first

* python manage.py shell
* from django.contrib.auth.models import User
* User.objects.get(username="admin", is_superuser=True).delete()


### Deployment

1. In Conatiner

* git clone https://Manishmbm2010@bitbucket.org/Manishmbm2010/home_banking_service_django_poc.git
* cd home_banking_service_django_poc/
* sudo docker-compose  -f docker-compose.yml up --build

2. Without Conatiner

* git clone https://Manishmbm2010@bitbucket.org/Manishmbm2010/home_banking_service_django_poc.git
* cd home_banking_service_django_poc/
* pip install -r requirements.txt
* python manage.py makemigrations customer
* python manage.py makemigrations account
* python manage.py makemigrations payments 
* python manage.py migrate
* python manage.py runserver


### Admin user and password

* user : admin
* pass : password



### Rest end points


* http://localhost:8000/customer/create 			(method=POST)
* request body : {"first_name":"Test_manish" ,"last_name":"Jain", "address":"Jain Temple","birth_date":"1993-10-28"}
* http://localhost:8000/customer/{id}				(method=GET)
* http://localhost:8000/customer/{id}				(method=PUT) 
* request body : {"first_name":"Test_manish" ,"last_name":"Jain", "address":"Jain Temple","birth_date":"2000-10-28"}
* http://localhost:8000/customer/{id}				(method=DELETE) 

* http://localhost:8000/account/create 				(method=POST)
* request body : {"customer_id":"1" ,"acc_type":"Credit_Card","acc_balance":"34.5"}
* http://localhost:8000/account/{id}				(method=GET)
* http://localhost:8000/account/{id}				(method=PUT) 
* request body : {"customer_id":"1", "acc_type":"Credit_Card","acc_balance":"50"}
* http://localhost:8000/account/{id}				(method=DELETE) 
* http://localhost:8000/account/getCustomerAccount/{customer_id}(method=GET) 

* http://localhost:8000/payment/create 				(method=POST)
* request body : {"originator_customer_id":1 ,"originator_acc_number":1, "transfer_amount":20,"beneficary_acc_number":5}
* http://localhost:8000/payment/{id}				(method=GET)
* http://localhost:8000/payment/{id}				(method=PUT) 
* request body : {"originator_customer_id":1 ,"originator_acc_number":1, "transfer_amount":30,"beneficary_acc_number":20}
* http://localhost:8000/payment/{id}				(method=DELETE) 



### Acknowledgments

Django has good documentation

* http://www.django-rest-framework.org/#tutorial
* https://docs.djangoproject.com/en/2.0/


### Scope for improvement 

* This solution can be extended with the usage of persistent storage.
* Exception handling can be improved.
* Logging can be enhanced.
* Comments can be added at many places to make the maintenace of code much simpler.

##Author

* **Manish Jain**


