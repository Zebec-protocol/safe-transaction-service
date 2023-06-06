# Generated by Django 4.2.1 on 2023-06-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0073_safecontract_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="SafeOwners",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("safe", models.CharField(max_length=225)),
                ("address", models.CharField(max_length=225)),
                ("name", models.CharField(max_length=225)),
            ],
            options={
                "verbose_name_plural": "Safe owners",
                "unique_together": {("safe", "address")},
            },
        ),
    ]
