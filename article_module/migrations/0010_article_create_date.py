# Generated by Django 5.1.1 on 2024-10-04 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0009_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2024, 10, 4), verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
    ]
