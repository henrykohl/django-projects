# Generated by Django 2.1.5 on 2023-07-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20230703_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(),
        ),
    ]
