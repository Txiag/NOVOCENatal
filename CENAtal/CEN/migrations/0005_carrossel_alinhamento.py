# Generated by Django 2.2.4 on 2019-10-01 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEN', '0004_carrossel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrossel',
            name='alinhamento',
            field=models.CharField(default='center', max_length=256),
            preserve_default=False,
        ),
    ]
