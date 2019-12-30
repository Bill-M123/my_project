from django.db import models

# Create your models here.

class Weekly_Picks(models.Model):
    """Model representing a book genre."""
    choice_id=models.AutoField(primary_key=True)
    player_name = models.TextField(max_length=30)
    week = models.TextField(max_length=20)
    game_num = models.IntegerField()
    home = models.TextField(max_length=20)
    away = models.TextField(max_length=20)
    spread = models.FloatField(null=True)
    prediction = models.TextField(max_length=20, help_text='Guess Winner')
    pred_points = models.IntegerField(null=True, help_text='Assign point value')
    pred_val = models.IntegerField(default=0)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Ladder_Picks(models.Model):
    """Model representing a book genre."""
    choice_id=models.AutoField(primary_key=True)
    player_name = models.TextField(max_length=30)
    week = models.TextField(max_length=20)
    game_num = models.IntegerField()
    home = models.TextField(max_length=20)
    away = models.TextField(max_length=20)
    gm_inp_1=models.BooleanField(null=True)
    gm_inp_1=models.BooleanField(null=True)


    def __str__(self):
        """String for representing the Model object."""
        return self.name
