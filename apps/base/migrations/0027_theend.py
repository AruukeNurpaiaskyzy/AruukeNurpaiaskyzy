# Generated by Django 5.1 on 2024-08-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'концы',
            },
        ),
    ]