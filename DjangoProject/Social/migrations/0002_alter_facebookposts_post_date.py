# Generated by Django 4.0.3 on 2022-03-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookposts',
            name='post_date',
            field=models.DateTimeField(null=True),
        ),
    ]