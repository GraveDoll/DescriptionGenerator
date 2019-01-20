# Generated by Django 2.0.3 on 2019-01-20 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0038_auto_20190120_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='length',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Length', verbose_name='丈'),
        ),
        migrations.AlterField(
            model_name='silhouette',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
    ]
