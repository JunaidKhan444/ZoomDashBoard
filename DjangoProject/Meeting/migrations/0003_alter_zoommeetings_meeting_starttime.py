# Generated by Django 4.0.3 on 2022-03-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0002_alter_zoommeetings_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoommeetings',
            name='meeting_starttime',
            field=models.DateTimeField(null=True),
        ),
    ]