# Generated by Django 4.2.4 on 2023-11-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quikform', '0010_resposta_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
