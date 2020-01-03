# Generated by Django 2.2.5 on 2019-12-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playoff_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playoff_Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(choices=[('BAL', 'Baltimore'), ('KC', 'Kansas City'), ('NE', 'New England'), ('HOU', 'Houston'), ('BUF', 'Buffalo'), ('Ten', 'Tennessee'), ('SF', 'San Francisco'), ('GB', 'Green Bay'), ('NO', 'New Orleans'), ('Phi', 'Philadelphia'), ('SEA', 'Seattle'), ('Min', 'Minnesota')], max_length=20)),
                ('seed', models.IntegerField()),
                ('division', models.CharField(choices=[('AFC', 'AFC'), ('NFC', 'NFC')], max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='ladder_picks',
            name='away',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ladder_picks',
            name='home',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ladder_picks',
            name='player_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ladder_picks',
            name='week',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='weekly_picks',
            name='away',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='weekly_picks',
            name='home',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='weekly_picks',
            name='player_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='weekly_picks',
            name='prediction',
            field=models.CharField(help_text='Guess Winner', max_length=20),
        ),
        migrations.AlterField(
            model_name='weekly_picks',
            name='week',
            field=models.CharField(max_length=20),
        ),
    ]