# Generated by Django 4.0.3 on 2022-09-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customer_file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
