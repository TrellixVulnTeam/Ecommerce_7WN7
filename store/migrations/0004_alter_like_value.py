# Generated by Django 4.0.6 on 2022-07-30 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('unlike', 'unlike'), ('like', 'like')], default='like', max_length=10),
        ),
    ]