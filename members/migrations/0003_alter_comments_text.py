# Generated by Django 4.1.2 on 2022-11-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0002_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="text",
            field=models.TextField(max_length=511),
        ),
    ]
