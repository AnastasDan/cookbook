# Generated by Django 3.2.3 on 2024-01-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20240126_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='times_used',
            field=models.IntegerField(default=0, editable=False, verbose_name='Количество использований продукта'),
        ),
    ]