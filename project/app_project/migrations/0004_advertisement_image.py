# Generated by Django 4.2.3 on 2023-08-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_project', '0003_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='project/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]
