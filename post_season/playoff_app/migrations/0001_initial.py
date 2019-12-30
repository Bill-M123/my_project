# Generated by Django 2.2.1 on 2019-12-30 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ladder_Picks',
            fields=[
                ('choice_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.TextField(max_length=30)),
                ('week', models.TextField(max_length=20)),
                ('game_num', models.IntegerField()),
                ('home', models.TextField(max_length=20)),
                ('away', models.TextField(max_length=20)),
                ('gm_inp_1', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_Picks',
            fields=[
                ('choice_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.TextField(max_length=30)),
                ('week', models.TextField(max_length=20)),
                ('game_num', models.IntegerField()),
                ('home', models.TextField(max_length=20)),
                ('away', models.TextField(max_length=20)),
                ('spread', models.FloatField(null=True)),
                ('prediction', models.TextField(help_text='Guess Winner', max_length=20)),
                ('pred_points', models.IntegerField(help_text='Assign point value', null=True)),
                ('pred_val', models.IntegerField(default=0)),
            ],
        ),
    ]