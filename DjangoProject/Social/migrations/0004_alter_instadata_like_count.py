# Generated by Django 4.0.3 on 2022-04-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0003_alter_instadata_comments_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instadata',
            name='like_count',
            field=models.IntegerField(null=True),
        ),
    ]