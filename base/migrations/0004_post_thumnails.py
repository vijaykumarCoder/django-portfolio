# Generated by Django 3.2.5 on 2021-08-31 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumnails',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]