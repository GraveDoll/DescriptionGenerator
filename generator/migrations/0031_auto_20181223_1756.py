# Generated by Django 2.0.3 on 2018-12-23 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0030_auto_20181223_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leg',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.MainCategory', verbose_name='メインカテゴリ'),
        ),
        migrations.AlterField(
            model_name='length',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.MainCategory', verbose_name='メインカテゴリ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='length',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Length', verbose_name='丈'),
        ),
    ]
