# Generated by Django 4.0.3 on 2022-03-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0003_alter_zoommeetings_meeting_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoommeetings',
            name='meeting_created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='zoommeetings',
            name='meeting_duration',
            field=models.IntegerField(null=True),
        ),
    ]
