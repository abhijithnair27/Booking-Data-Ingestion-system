## Booking Data Ingestion System

# To run the project follow the below steps - 

1. clone the repository.
2. create a virtual env using "python -m venv env"
3. setup your database by providing your credentials.
4. apply migrations- "python manage.py makemigrations" and then "python manage.py migrate"
5. to run use command - "python manage.py runserver"

# we have following set of API which we can call

1. GET /api/bookings/
2. POST /api/bookings
3. get by ID /api/bookings/<ID>
4. delete /api/bookings/<ID>/delete
    
