# Generated by Django 4.1.7 on 2023-03-03 03:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Phone number invalid', regex='(84|0[3|5|7|8|9])+([0-9]{8})\\b')]),
        ),
    ]
