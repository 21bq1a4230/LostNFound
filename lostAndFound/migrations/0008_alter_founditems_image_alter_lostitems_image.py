# Generated by Django 5.0.1 on 2024-06-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostAndFound', '0007_alter_founditems_image_alter_lostitems_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditems',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lostitems',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]