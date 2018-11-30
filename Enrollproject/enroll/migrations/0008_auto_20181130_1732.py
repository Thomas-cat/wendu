# Generated by Django 2.0.4 on 2018-11-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_auto_20181130_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yubaoming',
            name='exam_area',
            field=models.CharField(blank=True, choices=[('唐山市第十二中学(初中北院)', '唐山市第十二中学(初中北院)'), ('唐山市第二十六中学', '唐山市第二十六中学'), ('唐山市第三十中学(南校区)', '唐山市第三十中学(南校区)'), ('唐山市第五十二中学', '唐山市第五十二中学'), ('唐山市第五十四中学(主校区)', '唐山市第五十四中学(主校区)'), ('唐山市路北区七十号小学', '唐山市路北区七十号小学'), ('唐山市路北区龙泉西里小学', '唐山市路北区龙泉西里小学'), ('唐山市路北区扶轮小学', '唐山市路北区扶轮小学'), ('唐山市路北区鹭港小学', '唐山市路北区鹭港小学'), ('唐山市第一职业中', '唐山市第一职业中'), ('唐山市友谊中学(西校区)', '唐山市友谊中学(西校区)'), ('唐山市西山路小学', '唐山市西山路小学'), ('唐山师范学院附属小学', '唐山师范学院附属小学')], max_length=200, verbose_name='考点'),
        ),
    ]
