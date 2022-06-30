import apps.books_catalog.models
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.CharField(db_column='_id', default=apps.books_catalog.models.uuid_generator, editable=False, max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, verbose_name='name')),
                ('author', models.CharField(max_length=10, verbose_name='author')),
                ('category', models.CharField(max_length=50, verbose_name='category')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
