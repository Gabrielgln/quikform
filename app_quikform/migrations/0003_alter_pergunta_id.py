# Generated by Django 4.2.4 on 2023-10-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quikform', '0002_pergunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
