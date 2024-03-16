# Generated by Django 5.0.2 on 2024-02-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('original_image', models.ImageField(upload_to='images/')),
                ('enhanced_image', models.ImageField(blank=True, null=True, upload_to='enhanced/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
