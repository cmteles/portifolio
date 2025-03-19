# Generated by Django 4.2.19 on 2025-02-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=255, verbose_name='Assunto')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Edição')),
            ],
            options={
                'verbose_name': 'menssagem de contato',
                'verbose_name_plural': 'mensegens de contato',
            },
        ),
    ]
