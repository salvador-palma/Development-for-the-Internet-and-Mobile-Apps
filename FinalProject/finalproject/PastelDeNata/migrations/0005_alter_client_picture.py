# Generated by Django 4.2.11 on 2024-04-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PastelDeNata', '0004_alter_rating_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='picture',
            field=models.CharField(default='AvatarDefault', max_length=100, null=True),
        ),
    ]
