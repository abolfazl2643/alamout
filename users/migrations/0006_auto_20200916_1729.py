# Generated by Django 3.1 on 2020-09-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200901_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]