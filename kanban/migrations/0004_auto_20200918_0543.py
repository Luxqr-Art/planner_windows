# Generated by Django 3.1.1 on 2020-09-18 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0003_auto_20200918_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardcardcomments',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create Time'),
        ),
        migrations.AlterField(
            model_name='boardcards',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create Time'),
        ),
    ]
