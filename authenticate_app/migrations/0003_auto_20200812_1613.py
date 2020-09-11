# Generated by Django 3.0.3 on 2020-08-12 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate_app', '0002_jsoncontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsonContent',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authenticate_app.info'),
        ),
        migrations.AlterField(
            model_name='jsonContent',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='jsonContent',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
