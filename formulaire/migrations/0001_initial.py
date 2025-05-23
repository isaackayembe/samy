# Generated by Django 5.1.6 on 2025-04-04 11:39

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulaire.uniquelink')),
            ],
        ),
    ]
