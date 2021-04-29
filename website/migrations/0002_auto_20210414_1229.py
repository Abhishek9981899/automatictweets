# Generated by Django 3.1.7 on 2021-04-14 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='tweets',
            name='created',
        ),
        migrations.RemoveField(
            model_name='tweets',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tweets',
            name='updated',
        ),
        migrations.AddField(
            model_name='tweets',
            name='tweet_description',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweets',
            name='tweet_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweets',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweets',
            name='published',
            field=models.DateTimeField(),
        ),
    ]
