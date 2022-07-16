# Generated by Django 4.0.4 on 2022-06-26 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MascoApp', '0004_alter_cliente_edad_alter_cliente_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Producto'),
        ),
    ]