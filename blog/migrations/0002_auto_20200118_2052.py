# Generated by Django 3.0.1 on 2020-01-18 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogtype',
            old_name='blog_type',
            new_name='type_name',
        ),
    ]