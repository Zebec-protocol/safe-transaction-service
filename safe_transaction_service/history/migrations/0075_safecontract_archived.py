# Generated by Django 4.2.1 on 2023-06-23 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0074_safeowners"),
    ]

    operations = [
        migrations.AddField(
            model_name="safecontract",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
