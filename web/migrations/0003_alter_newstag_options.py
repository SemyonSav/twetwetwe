# Generated by Django 4.2.9 on 2024-01-30 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_newstag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newstag',
            options={'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
    ]
