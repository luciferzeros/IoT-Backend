# Generated by Django 3.1.3 on 2021-01-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_auto_20201215_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='chip',
            name='home',
            field=models.CharField(default='home1', max_length=100),
            preserve_default=False,
        ),
    ]
