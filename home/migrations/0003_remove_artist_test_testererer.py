# Generated by Django 4.0.2 on 2022-02-11 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_artist_test_testererer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artist",
            name="test_testererer",
        ),
    ]