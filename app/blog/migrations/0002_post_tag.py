# Generated by Django 2.1.1 on 2018-10-02 10:08

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]
