# Generated by Django 5.1.1 on 2024-09-14 17:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('ukuran', models.TextField()),
                ('aroma', models.TextField()),
                ('top_notes', models.TextField()),
                ('middle_notes', models.TextField()),
                ('base_notes', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MoodEntry',
        ),
    ]
