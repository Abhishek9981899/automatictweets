# Generated by Django 3.1.7 on 2021-04-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210414_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='published',
            field=models.DateField(),
        ),
    ]