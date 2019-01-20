# Generated by Django 2.0.3 on 2018-11-17 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0009_auto_20180815_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='メインカテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='性別')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='サブカテゴリ名')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.MainCategory', verbose_name='メインカテゴリ')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Sex', verbose_name='カテゴリ'),
        ),
        migrations.AddField(
            model_name='maincategory',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='generator.Sex', verbose_name='性別'),
        ),
    ]