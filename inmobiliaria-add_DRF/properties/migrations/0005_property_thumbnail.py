# Generated by Django 4.2.2 on 2024-04-16 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_propertybuy'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='thumbs'),
        ),
    ]
