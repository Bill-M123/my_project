# Generated by Django 2.2.5 on 2019-12-30 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playoff_app', '0004_auto_20191230_1052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playoff_team',
            options={'ordering': ('division', 'seed')},
        ),
        migrations.AddField(
            model_name='ladder_pick',
            name='pred_winner',
            field=models.CharField(default=3, max_length=20),
            preserve_default=False,
        ),
    ]