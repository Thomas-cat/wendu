# Generated by Django 2.0.4 on 2018-12-01 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0008_auto_20181130_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='yubaoming',
            name='is_enroll',
            field=models.BooleanField(default=False, verbose_name='已报名'),
        ),
    ]
