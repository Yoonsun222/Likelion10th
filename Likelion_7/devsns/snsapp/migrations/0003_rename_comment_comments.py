# Generated by Django 3.2.14 on 2022-07-13 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0002_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
