# Generated by Django 2.2.5 on 2019-12-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20191112_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=1, upload_to='images/ava', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
