# Generated by Django 3.0.6 on 2020-06-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minecraft', '0007_auto_20200602_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcserver',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thmbnails'),
        ),
    ]