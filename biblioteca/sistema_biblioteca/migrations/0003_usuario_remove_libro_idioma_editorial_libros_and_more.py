# Generated by Django 4.2.1 on 2023-05-18 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_biblioteca', '0002_editorial_genero_autor_nacionalidad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=80, verbose_name='Apellido')),
                ('mail', models.EmailField(max_length=128, verbose_name='Email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='libro',
            name='idioma',
        ),
        migrations.AddField(
            model_name='editorial',
            name='Libros',
            field=models.ManyToManyField(to='sistema_biblioteca.libro'),
        ),
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.CharField(default='Descripcion', max_length=3000, verbose_name='Descripcion'),
        ),
        migrations.AddField(
            model_name='libro',
            name='genero',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sistema_biblioteca.genero'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='genero',
            field=models.CharField(default='Género', max_length=20, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sistema_biblioteca.autor'),
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=20, verbose_name='Idioma')),
                ('Libros', models.ManyToManyField(to='sistema_biblioteca.libro')),
            ],
        ),
    ]
