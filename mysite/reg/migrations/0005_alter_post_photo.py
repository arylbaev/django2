# Generated by Django 4.2.7 on 2023-11-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
