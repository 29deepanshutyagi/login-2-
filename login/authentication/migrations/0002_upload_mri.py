# Generated by Django 4.2.4 on 2023-10-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='mri',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
