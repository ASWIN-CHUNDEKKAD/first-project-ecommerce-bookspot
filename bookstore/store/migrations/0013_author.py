# Generated by Django 4.2.5 on 2023-10-12 04:24

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_category_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('author_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
