# Generated by Django 4.2.13 on 2024-07-01 10:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loginsystem", "0006_remove_profile_profile_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                blank=True, null=True, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="courses",
            field=models.ManyToManyField(blank=True, to="loginsystem.course"),
        ),
    ]
