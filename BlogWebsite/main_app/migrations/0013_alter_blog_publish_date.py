# Generated by Django 4.2.1 on 2023-06-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_blog_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
