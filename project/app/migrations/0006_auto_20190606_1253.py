# Generated by Django 2.2.1 on 2019-06-06 07:23

import app.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_parents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parents',
            old_name='par_frist_name',
            new_name='parent_frist_name',
        ),
        migrations.RenameField(
            model_name='parents',
            old_name='par_last_name',
            new_name='parent_last_name',
        ),
        migrations.AddField(
            model_name='parents',
            name='Student_Attendence_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name=app.models.Student_Attendance),
        ),
        migrations.AddField(
            model_name='parents',
            name='present',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parents',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Parents_student', to=settings.AUTH_USER_MODEL),
        ),
    ]