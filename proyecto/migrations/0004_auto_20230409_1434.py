# Generated by Django 3.2.18 on 2023-04-09 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0003_plancapacidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preventa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='plancapacidad',
            name='preventa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.preventa'),
        ),
    ]