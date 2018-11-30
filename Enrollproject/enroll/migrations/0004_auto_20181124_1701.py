# Generated by Django 2.0.4 on 2018-11-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_yubaoming_modifed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='yubaoming',
            name='is_pay',
            field=models.BooleanField(default=True, verbose_name='预报名支付'),
        ),
        migrations.AlterField(
            model_name='yubaoming',
            name='major',
            field=models.CharField(choices=[('医学', '医学'), ('建工', '建工'), ('其它', '其它'), ('管联', '管联')], max_length=10, verbose_name='专业'),
        ),
    ]