# Generated by Django 5.2 on 2025-04-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariods16',
            name='animais',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
