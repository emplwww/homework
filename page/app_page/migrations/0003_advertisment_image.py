# Generated by Django 4.2.3 on 2023-08-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_page', '0002_advertisment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='image',
            field=models.ImageField(default='', upload_to='page/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]
