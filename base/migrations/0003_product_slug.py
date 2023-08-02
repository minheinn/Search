# Generated by Django 4.2.3 on 2023-08-02 02:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]