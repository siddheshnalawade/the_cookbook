# Generated by Django 3.0.6 on 2021-04-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='display_image',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]