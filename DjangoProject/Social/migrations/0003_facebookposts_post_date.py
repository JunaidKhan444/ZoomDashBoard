# Generated by Django 4.0.3 on 2022-03-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0002_remove_facebookposts_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookposts',
            name='post_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]