# Generated by Django 2.0.3 on 2019-01-27 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0040_auto_20190120_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='silhouettedescription',
            name='parent',
        ),
        migrations.AlterField(
            model_name='post',
            name='length',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Length', verbose_name='丈'),
        ),
        migrations.DeleteModel(
            name='SilhouetteDescription',
        ),
    ]
