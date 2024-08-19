# Generated by Django 5.1 on 2024-08-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_action_alter_about_options_alter_about_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='actional_image', verbose_name='фотки')),
            ],
            options={
                'verbose_name': 'фотографии',
                'verbose_name_plural': 'фотографии',
            },
        ),
    ]