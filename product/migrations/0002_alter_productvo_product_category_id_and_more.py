# Generated by Django 5.1.6 on 2025-03-10 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_created_on_categoryvo_create_at_and_more'),
        ('product', '0001_initial'),
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvo',
            name='product_category_id',
            field=models.ForeignKey(db_column='product_category_vo', on_delete=django.db.models.deletion.PROTECT, to='category.categoryvo'),
        ),
        migrations.AlterField(
            model_name='productvo',
            name='product_subcategory_id',
            field=models.ForeignKey(db_column='product_subcategory_vo', on_delete=django.db.models.deletion.PROTECT, to='subcategory.subcategoryvo'),
        ),
    ]
