# python_books_catalog
Books Catalog 

Create a virtual environment
python3 -m venv venv1

Activate virtual environment
source/venv1/bin/activate

Make Migrations
python3 src/manage.py makemigrations books

Migrate
python3 src/manage.py migrate

Run Server
python3 src/manage.py runserver