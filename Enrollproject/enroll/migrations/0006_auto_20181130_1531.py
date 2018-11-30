# Generated by Django 2.0.4 on 2018-11-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_auto_20181124_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormalEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('modifed_date', models.DateTimeField(auto_now_add=True, verbose_name='报名时间')),
                ('need_dorm', models.CharField(choices=[('单人间', '单人间'), ('双人间', '双人间')], max_length=10, verbose_name='酒店')),
                ('area', models.CharField(choices=[('市区', '市区'), ('曹妃甸', '曹妃甸')], max_length=10, verbose_name='地点')),
                ('need_bus', models.CharField(choices=[('单程去', '单程去'), ('双程', '双程'), ('不需要', '不需要')], max_length=10, verbose_name='大巴车')),
                ('need_lunch', models.CharField(blank=True, choices=[('1天', '1天'), ('2天', '2天'), ('不需要', '不需要')], max_length=10, verbose_name='午餐')),
                ('sex', models.CharField(blank=True, choices=[('男生', '男生'), ('女生', '女生')], max_length=4, verbose_name='性别')),
                ('major', models.CharField(choices=[('医学', '医学'), ('建工', '建工'), ('其它', '其它'), ('管联', '管联')], max_length=10, verbose_name='专业')),
                ('day_dorm', models.CharField(blank=True, choices=[('1天', '1天'), ('2天', '2天')], max_length=4, verbose_name='住宿天数')),
                ('money', models.CharField(blank=True, max_length=4, verbose_name='金额')),
                ('all_pay', models.BooleanField(default=False, verbose_name='完成支付')),
                ('is_pay', models.BooleanField(default=False, verbose_name='完成预报名支付')),
                ('is_enroll', models.BooleanField(default=False, verbose_name='是否预报名')),
            ],
            options={
                'verbose_name_plural': '12月正式报名',
            },
        ),
        migrations.AddField(
            model_name='yubaoming',
            name='all_pay',
            field=models.BooleanField(default=False, verbose_name='完成支付'),
        ),
        migrations.AddField(
            model_name='yubaoming',
            name='day_dorm',
            field=models.CharField(blank=True, choices=[('1天', '1天'), ('2天', '2天'), ('不需要', '不需要')], max_length=4, verbose_name='住宿天数'),
        ),
        migrations.AddField(
            model_name='yubaoming',
            name='money',
            field=models.CharField(blank=True, max_length=4, verbose_name='金额'),
        ),
        migrations.AddField(
            model_name='yubaoming',
            name='sex',
            field=models.CharField(blank=True, choices=[('男生', '男生'), ('女生', '女生')], max_length=4, verbose_name='性别'),
        ),
    ]