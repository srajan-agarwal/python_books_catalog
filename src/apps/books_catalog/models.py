import uuid
from django.db import models

# Create your models here

def uuid_generator():
    return str(uuid.uuid4()).replace("-", "")

class Books(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=uuid_generator, editable=False, db_column='_id')
    name = models.CharField("name", max_length=70, blank=False, null=False)
    author = models.CharField("author", max_length=10, blank=False, null=False)
    category = models.CharField("category", max_length=50, blank=False, null=False)
    title = models.CharField("title", max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'books'
