# python_books_catalog
Books Catalog 
Here the code creates an API to create books and add them to a MySQL table using Django Rest Framework

Steps to Run:- 

1. Create a virtual environment
python3 -m venv venv1

2. Activate virtual environment
source/venv1/bin/activate

3. Make Migrations
python3 src/manage.py makemigrations books

4. Migrate
python3 src/manage.py migrate

Run Server
python3 src/manage.py runserver