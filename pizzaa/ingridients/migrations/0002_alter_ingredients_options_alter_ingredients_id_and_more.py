# Generated by Django 4.2.4 on 2023-08-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingridients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredients',
            options={'verbose_name': 'Ingredients', 'verbose_name_plural': 'Ingredients'},
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='type',
            field=models.CharField(choices=[('Dough', 'Dough'), ('Spicery', 'Spicery'), ('Sauce', 'Sauce'), ('Meat_products', 'Meat Products'), ('Cheese', 'Cheese')], max_length=20),
        ),
    ]
