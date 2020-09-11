# Generated by Django 3.0.3 on 2020-08-13 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate_app', '0005_delete_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsonContent',
            name='upload',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
