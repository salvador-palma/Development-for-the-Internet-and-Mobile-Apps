# Generated by Django 4.2.11 on 2024-04-12 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PastelDeNata', '0005_alter_client_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.TextField(default='Sem descrição ainda...', null=True),
        ),
    ]
