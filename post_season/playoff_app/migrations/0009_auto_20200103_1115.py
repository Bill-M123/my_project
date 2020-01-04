# Generated by Django 2.2.1 on 2020-01-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playoff_app', '0008_game_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_schedule',
            name='dog',
            field=models.CharField(choices=[('BAL', 'Baltimore'), ('KC', 'Kansas City'), ('NE', 'New England'), ('HOU', 'Houston'), ('BUF', 'Buffalo'), ('TEN', 'Tennessee'), ('SF', 'San Francisco'), ('GB', 'Green Bay'), ('NO', 'New Orleans'), ('PHI', 'Philadelphia'), ('SEA', 'Seattle'), ('MIN', 'Minnesota')], default='None', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game_schedule',
            name='game_num',
            field=models.IntegerField(default=0),
        ),
    ]