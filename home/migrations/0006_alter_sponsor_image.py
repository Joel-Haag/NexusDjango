# Generated by Django 4.0.2 on 2022-02-12 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_sponsor_sponsorimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsor",
            name="image",
            field=models.FileField(upload_to="images/"),
        ),
    ]