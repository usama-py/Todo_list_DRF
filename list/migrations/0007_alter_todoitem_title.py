# Generated by Django 4.2.1 on 2023-06-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("list", "0006_alter_todoitem_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="title",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
