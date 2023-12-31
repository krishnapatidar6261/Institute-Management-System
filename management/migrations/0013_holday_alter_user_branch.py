# Generated by Django 4.2.4 on 2023-10-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_alter_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_name', models.CharField(max_length=50)),
                ('holiday_type', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.CharField(choices=[('CSA', 'CSA'), ('agreeculture', 'agreeculture'), ('pharmacy', 'pharmacy')], max_length=50),
        ),
    ]
