# Generated by Django 5.0.1 on 2024-06-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostAndFound', '0004_auto_20240617_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditems',
            name='image',
            field=models.ImageField(default=None, upload_to='founditems'),
        ),
        migrations.AddField(
            model_name='lostitems',
            name='image',
            field=models.ImageField(default=None, upload_to='lostitems'),
        ),
    ]
