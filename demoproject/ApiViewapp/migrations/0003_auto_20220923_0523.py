# Generated by Django 3.1 on 2022-09-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiViewapp', '0002_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
