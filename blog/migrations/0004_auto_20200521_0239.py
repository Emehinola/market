# Generated by Django 3.0.6 on 2020-05-21 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200521_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog'),
        ),
    ]
