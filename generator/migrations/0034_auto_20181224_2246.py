# Generated by Django 2.0.3 on 2018-12-24 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0033_auto_20181224_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='effect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Effect', verbose_name='加工'),
        ),
        migrations.AlterField(
            model_name='post',
            name='leg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Leg', verbose_name='膝下'),
        ),
        migrations.AlterField(
            model_name='post',
            name='length',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Length', verbose_name='丈'),
        ),
    ]
