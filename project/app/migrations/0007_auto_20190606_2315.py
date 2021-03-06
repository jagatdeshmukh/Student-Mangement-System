# Generated by Django 2.2.1 on 2019-06-06 17:45

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190606_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parents',
            old_name='parent_frist_name',
            new_name='frist_name',
        ),
        migrations.RenameField(
            model_name='parents',
            old_name='parent_last_name',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='exam',
            name='student_marks',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parents',
            name='student_marks',
            field=models.FloatField(verbose_name=app.models.Exam),
        ),
        migrations.AlterField(
            model_name='parents',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
