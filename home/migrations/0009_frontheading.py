# Generated by Django 4.0.2 on 2022-02-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_frontimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="FrontHeading",
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
                ("title", models.CharField(max_length=200)),
                ("first_line", models.CharField(max_length=200)),
                ("second_line", models.CharField(max_length=200)),
                ("list_order", models.IntegerField()),
            ],
        ),
    ]
