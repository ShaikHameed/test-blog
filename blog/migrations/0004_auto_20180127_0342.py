# Generated by Django 2.0.1 on 2018-01-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180127_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='paragraph_image',
            field=models.CharField(blank=True, max_length=3000),
        ),
    ]
