# Generated by Django 4.2.18 on 2025-02-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_bookinstance_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="date_of_death",
            field=models.DateField(blank=True, null=True, verbose_name="died"),
        ),
    ]
