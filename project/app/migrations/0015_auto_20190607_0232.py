# Generated by Django 2.2.1 on 2019-06-06 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190607_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendence',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]