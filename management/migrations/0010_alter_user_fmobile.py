# Generated by Django 4.2.3 on 2023-08-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_alter_user_branch_alter_user_father_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fmobile',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
