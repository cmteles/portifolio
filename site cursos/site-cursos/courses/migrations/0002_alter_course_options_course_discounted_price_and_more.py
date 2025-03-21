# Generated by Django 5.1.6 on 2025-02-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_create_courses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='course',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço com Desconto'),
        ),
        migrations.AddField(
            model_name='course',
            name='original_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço Original'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='course',
            name='upadated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de modificação'),
        ),
    ]
