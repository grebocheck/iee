# Generated by Django 2.2.5 on 2020-01-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_member_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_post',
            field=models.DateTimeField(verbose_name='Дата створення посту'),
        ),
    ]