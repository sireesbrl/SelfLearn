# Generated by Django 4.2.13 on 2024-07-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapters",
            name="path",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
