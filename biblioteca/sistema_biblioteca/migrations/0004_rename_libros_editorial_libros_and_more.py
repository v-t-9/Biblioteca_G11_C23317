# Generated by Django 4.2.1 on 2023-05-19 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_biblioteca', '0003_usuario_remove_libro_idioma_editorial_libros_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editorial',
            old_name='Libros',
            new_name='libros',
        ),
        migrations.RenameField(
            model_name='idioma',
            old_name='Libros',
            new_name='libros',
        ),
    ]
