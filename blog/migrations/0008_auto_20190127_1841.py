# Generated by Django 2.1.5 on 2019-01-27 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190127_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='created',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='created',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='updated',
        ),
    ]
