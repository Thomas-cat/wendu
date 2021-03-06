# Generated by Django 2.0.4 on 2018-10-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('qq', models.CharField(blank=True, max_length=12)),
                ('obj_school', models.CharField(blank=True, max_length=100, verbose_name='目标学校')),
                ('institute', models.CharField(blank=True, max_length=100, verbose_name='所在学院')),
                ('major', models.CharField(blank=True, max_length=100, verbose_name='所在专业')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('is_enroll', models.BooleanField(verbose_name='是否学员')),
                ('modifed_date', models.DateTimeField(auto_now_add=True, verbose_name='信息提交时间')),
            ],
            options={
                'verbose_name_plural': '文都直通车信息表',
            },
        ),
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('qq', models.CharField(max_length=12)),
                ('obj_school', models.CharField(max_length=100, verbose_name='报考学校')),
                ('obj_major', models.CharField(max_length=100, verbose_name='报考专业')),
                ('major', models.CharField(max_length=100, verbose_name='所在专业')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('is_return', models.CharField(max_length=40, verbose_name='是否往返')),
                ('is_need', models.BooleanField(verbose_name='12月份是否需要提供服务')),
                ('is_enroll', models.CharField(max_length=4, verbose_name='是否学员')),
                ('sex', models.CharField(max_length=10, verbose_name='性别')),
                ('modifed_date', models.DateTimeField(auto_now_add=True, verbose_name='信息提交时间')),
                ('ride_date', models.CharField(max_length=20, verbose_name='乘车日期')),
                ('ride_time', models.CharField(max_length=20, verbose_name='乘车班次')),
                ('price', models.CharField(max_length=4, verbose_name='票价')),
            ],
            options={
                'verbose_name_plural': '文都现场确认信息表',
            },
        ),
    ]
