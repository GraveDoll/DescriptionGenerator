# Generated by Django 2.0.3 on 2018-07-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0005_auto_20180428_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_category_1',
            field=models.CharField(blank=True, choices=[('シャツ', 'トップス'), ('カットソー', 'トップス'), ('ポロシャツ', 'トップス'), ('タンクトップ', 'トップス'), ('ニット/セーター', 'トップス'), ('パーカー', 'トップス'), ('カーディガン', 'トップス'), ('スウェット', 'トップス'), ('ジャージ', 'トップス'), ('ベスト', 'トップス'), ('その他', 'トップス'), ('デニムパンツ', 'パンツ'), ('カーゴパンツ', 'パンツ')], max_length=128, verbose_name='サブカテゴリ1'),
        ),
    ]
