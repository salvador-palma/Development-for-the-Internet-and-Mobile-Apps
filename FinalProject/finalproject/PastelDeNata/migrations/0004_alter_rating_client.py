# Generated by Django 4.2.11 on 2024-04-11 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PastelDeNata', '0003_remove_rating_user_client_rating_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PastelDeNata.client'),
        ),
    ]
