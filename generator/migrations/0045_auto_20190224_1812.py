# Generated by Django 2.0.3 on 2019-02-24 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0044_auto_20190224_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='coller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Coller', verbose_name='襟'),
        ),
        migrations.AlterField(
            model_name='post',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Design', verbose_name='デザイン'),
        ),
        migrations.AlterField(
            model_name='post',
            name='length',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Length', verbose_name='丈'),
        ),
        migrations.AlterField(
            model_name='post',
            name='neck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Neck', verbose_name='ネック'),
        ),
        migrations.AlterField(
            model_name='post',
            name='silhouette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Silhouette', verbose_name='シルエット'),
        ),
    ]
