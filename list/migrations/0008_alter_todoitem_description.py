# Generated by Django 4.2.1 on 2023-06-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("list", "0007_alter_todoitem_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="description",
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
