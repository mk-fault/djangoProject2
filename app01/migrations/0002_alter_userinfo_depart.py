# Generated by Django 4.1.3 on 2023-03-07 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="depart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app01.department"
            ),
        ),
    ]
