# Generated by Django 4.0.3 on 2022-03-29 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoryTupe',
            new_name='categoryType',
        ),
    ]