# Generated by Django 5.0.1 on 2024-06-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostAndFound', '0005_founditems_image_lostitems_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditems',
            name='image',
            field=models.ImageField(default=None, upload_to='founditems/'),
        ),
        migrations.AlterField(
            model_name='lostitems',
            name='image',
            field=models.ImageField(default=None, upload_to='lostitems/'),
        ),
    ]
