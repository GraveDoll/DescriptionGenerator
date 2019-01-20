# Generated by Django 2.0.3 on 2018-12-16 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0026_auto_20181202_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='LENGTH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.CharField(choices=[('ひざ上', 'ひざ上'), ('ひざ丈', 'ひざ丈'), ('クロップド', 'クロップド'), ('フルレングス', 'フルレングス'), ('ショート・ミニ丈', 'ショート・ミニ丈'), ('ひざ丈', 'ひざ丈'), ('ロング・マキシ丈', 'ロング・マキシ丈'), ('ミモレ・半端丈', 'ミモレ・半端丈')], max_length=255)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.SubCategory', verbose_name='サブカテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='ZIP_BUTTON',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_button', models.CharField(choices=[('プルオーバー', 'パーカー'), ('ジップアップ', 'パーカー')], max_length=255)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.SubCategory', verbose_name='サブカテゴリ')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='coller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.COLLER', verbose_name='襟'),
        ),
        migrations.AlterField(
            model_name='post',
            name='neck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.NECK', verbose_name='ネック'),
        ),
        migrations.AddField(
            model_name='post',
            name='length',
            field=models.ForeignKey(default='', max_length=255, on_delete=django.db.models.deletion.PROTECT, to='generator.LENGTH', verbose_name='丈'),
        ),
        migrations.AddField(
            model_name='post',
            name='zip_button',
            field=models.ForeignKey(default='', max_length=255, on_delete=django.db.models.deletion.PROTECT, to='generator.ZIP_BUTTON', verbose_name='ジップ・ボタン'),
        ),
    ]
