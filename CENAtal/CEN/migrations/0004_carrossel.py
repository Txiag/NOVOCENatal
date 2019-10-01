# Generated by Django 2.2.4 on 2019-10-01 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CEN', '0003_noticia_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrossel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.TextField()),
                ('titulo', models.CharField(max_length=256)),
                ('descricao', models.TextField()),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CEN.Noticia')),
            ],
        ),
    ]