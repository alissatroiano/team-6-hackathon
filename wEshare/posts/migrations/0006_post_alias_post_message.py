# Generated by Django 4.0 on 2022-01-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_status_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alias',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]