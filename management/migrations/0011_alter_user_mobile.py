# Generated by Django 4.2.3 on 2023-08-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_alter_user_fmobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
