# Generated by Django 3.0.3 on 2020-09-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textsum_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsoncontent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
