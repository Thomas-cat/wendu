# Generated by Django 2.0.4 on 2018-12-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0010_auto_20181201_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yubaoming',
            name='day_dorm',
            field=models.CharField(blank=True, choices=[('1天', '1天'), ('2天', '2天')], max_length=4, verbose_name='住宿天数'),
        ),
    ]
