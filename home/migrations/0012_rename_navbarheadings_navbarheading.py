# Generated by Django 4.0.2 on 2022-02-16 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_navbarheadings"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NavbarHeadings",
            new_name="NavbarHeading",
        ),
    ]
