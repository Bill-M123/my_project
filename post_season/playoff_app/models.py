from django.db import models

# Create your models here.

class Playoff_Team(models.Model):
    TEAMS=(('BAL','Baltimore'),('KC','Kansas City'),('NE','New England'),
    ('HOU','Houston'),('BUF','Buffalo'),('TEN','Tennessee'),
    ('SF','San Francisco'),('GB','Green Bay'),('NO','New Orleans'),
    ('PHI','Philadelphia'),('SEA','Seattle'),('MIN','Minnesota'))

    DIVISION=(('AFC','AFC'),('NFC','NFC'))

    GMSCHEDULE=(('AFC_WC1','Game1'),('AFC_WC2','Game2'),('NFC_WC1','Game3'),('NFC_WC2','Game4'),
    ('AFC_DIV1','Game5'),('AFC_DIV2','Game6'),('NFC_DIV1','Game7'),('NFC_DIV2','Game8'),
    ('AFC_Championship','Game9'),('NFC_Championship','Game10'),
    ('Superbowl','Game11'),('BYE','BYE'))

    team = models.CharField(max_length=20, choices=TEAMS)
    seed = models.IntegerField()
    division = models.CharField(max_length=3, choices=DIVISION)
    next_game = models.CharField(max_length=16, choices=GMSCHEDULE,default="BYE")

    class Meta:
        ordering = ('division', 'seed', )

class Weekly_Pick(models.Model):
    """Model representing a book genre."""
    choice_id=models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=30)

    WEEKS=(('WC','Wildcard'),('DIV','Division'),('CON','Conference'),('SB','Superbowl'))
    week = models.CharField(max_length=3, choices=WEEKS)
    game_num = models.IntegerField()

    TEAMS=(('BAL','Baltimore'),('KC','Kansas City'),('NE','New England'),
    ('HOU','Houston'),('BUF','Buffalo'),('Ten','Tennessee'),
    ('SF','San Francisco'),('GB','Green Bay'),('NO','New Orleans'),
    ('Phi','Philadelphia'),('SEA','Seattle'),('Min','Minnesota'))
    home = models.CharField(max_length=20, choices=TEAMS)
    away = models.CharField(max_length=20, choices=TEAMS)
    spread = models.FloatField(null=True)
    prediction = models.CharField(max_length=20, help_text='Guess Winner')
    pred_points = models.IntegerField(null=True, help_text='Assign point value')
    pred_val = models.IntegerField(default=0)

    def __str__(self):
        """String for representing the Model object."""
        return self.player_name

class Ladder_Pick(models.Model):
    """Model representing a book genre."""
    choice_id=models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=30)
    week = models.CharField(max_length=20)
    game_num = models.IntegerField()
    home = models.CharField(max_length=20)
    away = models.CharField(max_length=20)
    pred_winner = models.CharField(max_length=20)
    gm_inp_1=models.BooleanField(null=True)
    gm_inp_1=models.BooleanField(null=True)


    def __str__(self):
        """String for representing the Model object."""
        return self.player_name
