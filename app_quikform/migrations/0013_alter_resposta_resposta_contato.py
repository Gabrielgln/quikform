# Generated by Django 4.2.4 on 2023-11-23 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_quikform', '0012_alter_resposta_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='resposta',
            field=models.TextField(default='', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.TextField(max_length=100)),
                ('comentario', models.TextField(max_length=255)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
