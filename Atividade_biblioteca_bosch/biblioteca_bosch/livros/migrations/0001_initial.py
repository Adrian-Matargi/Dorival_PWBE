# Generated by Django 5.1.7 on 2025-03-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('ano_publicacao', models.IntegerField()),
                ('descricao', models.TextField()),
            ],
        ),
    ]
