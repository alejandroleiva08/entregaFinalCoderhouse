# Generated by Django 4.2.3 on 2023-07-20 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]