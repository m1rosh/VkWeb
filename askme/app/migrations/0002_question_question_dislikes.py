# Generated by Django 4.2.6 on 2023-11-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_dislikes',
            field=models.IntegerField(default=0),
        ),
    ]
