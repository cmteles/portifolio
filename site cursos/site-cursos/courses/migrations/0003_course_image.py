# Generated by Django 5.1.6 on 2025-02-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_options_course_discounted_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/', verbose_name='Imagem'),
        ),
    ]
