# Generated by Django 4.2.4 on 2023-10-17 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quikform', '0006_formulario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField(max_length=255)),
            ],
        ),
    ]
