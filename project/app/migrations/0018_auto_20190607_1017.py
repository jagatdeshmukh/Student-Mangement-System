# Generated by Django 2.2.1 on 2019-06-07 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20190607_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='Course',
            new_name='course',
        ),
    ]
