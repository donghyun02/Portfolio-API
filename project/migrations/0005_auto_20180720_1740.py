# Generated by Django 2.0.7 on 2018-07-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20180718_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]