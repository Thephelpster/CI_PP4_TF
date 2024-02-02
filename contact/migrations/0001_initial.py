# Generated by Django 3.2.15 on 2024-02-01 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('message', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]