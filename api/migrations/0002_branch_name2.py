# Generated by Django 5.1.3 on 2024-11-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='name2',
            field=models.CharField(default='', max_length=21),
            preserve_default=False,
        ),
    ]