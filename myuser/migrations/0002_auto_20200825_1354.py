# Generated by Django 3.1 on 2020-08-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='homepage',
            field=models.URLField(blank=True, null=True),
        ),
    ]
