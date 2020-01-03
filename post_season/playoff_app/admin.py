from django.contrib import admin

# Register your models here.
from .models import Weekly_Pick, Ladder_Pick, Playoff_Team

#admin.site.register(Weekly_Pick)
admin.site.register(Ladder_Pick)
#admin.site.register(Playoff_Teams)
# Define the admin class
class Playoff_TeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'seed', 'division','next_game')

class Weekly_PickAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'week', 'game_num','home','away',
    'spread','prediction','pred_points')

    list_filter = ('player_name', 'week')

class Ladder_PickAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'week', 'game_num','home','away',
    'spread','prediction','pred_points')

# Register the admin class with the associated model
admin.site.register(Playoff_Team, Playoff_TeamAdmin)
admin.site.register(Weekly_Pick,Weekly_PickAdmin)
