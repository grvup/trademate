# Generated by Django 4.1.13 on 2024-07-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_alter_history_csv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='csv_file',
            field=models.FileField(upload_to='csv_files/'),
        ),
    ]
