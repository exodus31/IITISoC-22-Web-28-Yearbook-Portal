# Generated by Django 4.0.5 on 2022-07-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='img',
            field=models.ImageField(default='x', upload_to=''),
        ),
    ]
