# Generated by Django 2.2.1 on 2019-06-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.ManyToManyField(to='app.Subject'),
        ),
    ]