# Generated by Django 2.1.5 on 2019-01-29 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_auto_20190128_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploads',
            name='uploaded_file',
            field=models.FileField(upload_to='image/'),
        ),
    ]
