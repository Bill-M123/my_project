# Generated by Django 2.2.1 on 2020-01-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playoff_app', '0007_auto_20200101_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_num', models.IntegerField()),
                ('home', models.CharField(choices=[('BAL', 'Baltimore'), ('KC', 'Kansas City'), ('NE', 'New England'), ('HOU', 'Houston'), ('BUF', 'Buffalo'), ('TEN', 'Tennessee'), ('SF', 'San Francisco'), ('GB', 'Green Bay'), ('NO', 'New Orleans'), ('PHI', 'Philadelphia'), ('SEA', 'Seattle'), ('MIN', 'Minnesota')], max_length=20)),
                ('away', models.CharField(choices=[('BAL', 'Baltimore'), ('KC', 'Kansas City'), ('NE', 'New England'), ('HOU', 'Houston'), ('BUF', 'Buffalo'), ('TEN', 'Tennessee'), ('SF', 'San Francisco'), ('GB', 'Green Bay'), ('NO', 'New Orleans'), ('PHI', 'Philadelphia'), ('SEA', 'Seattle'), ('MIN', 'Minnesota')], max_length=20)),
                ('spread', models.FloatField(null=True)),
            ],
        ),
    ]