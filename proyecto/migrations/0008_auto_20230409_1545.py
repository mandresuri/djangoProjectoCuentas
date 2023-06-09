# Generated by Django 3.2.18 on 2023-04-09 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0007_auto_20230409_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plancapacidad',
            old_name='Comercial',
            new_name='comercial',
        ),
        migrations.AlterField(
            model_name='plancapacidad',
            name='productos',
            field=models.ManyToManyField(blank=True, to='proyecto.Producto'),
        ),
        migrations.CreateModel(
            name='PlanCapacidadServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.FloatField()),
                ('precio', models.FloatField()),
                ('plancapacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.plancapacidad')),
                ('servicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.servicio')),
            ],
        ),
        migrations.AlterField(
            model_name='plancapacidad',
            name='servicios',
            field=models.ManyToManyField(blank=True, through='proyecto.PlanCapacidadServicio', to='proyecto.Servicio'),
        ),
    ]
