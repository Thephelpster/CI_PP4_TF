# Generated by Django 4.2.9 on 2024-01-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                ("food_id", models.AutoField(primary_key=True, serialize=False)),
                ("food_name", models.CharField(max_length=50, unique=True)),
                ("description", models.CharField(max_length=300, unique=True)),
                ("price", models.FloatField()),
                (
                    "type_of_food",
                    models.IntegerField(
                        choices=[
                            (0, "Starters"),
                            (1, "Mains"),
                            (2, "Desserts"),
                            (3, "New"),
                        ],
                        default=3,
                    ),
                ),
                ("available", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["-type_of_food"],
            },
        ),
    ]