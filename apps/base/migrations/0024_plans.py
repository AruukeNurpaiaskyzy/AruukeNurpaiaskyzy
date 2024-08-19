# Generated by Django 5.1 on 2024-08-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_design'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название плана')),
                ('description', models.TextField(verbose_name='описание плана')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'планы',
            },
        ),
    ]
