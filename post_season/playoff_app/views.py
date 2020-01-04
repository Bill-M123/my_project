from django.shortcuts import render

from playoff_app.models import Playoff_Team, Weekly_Pick, Ladder_Pick,Game_Schedule



def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_teams = Playoff_Team.objects.all().count()
    num_picks = Weekly_Pick.objects.all().count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    context = {
        'num_teams': num_teams,
        'num_picks': num_picks,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def Leaderboard(request):
    """View function for Leaderboard page of site."""

    context = {}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'leaderboard.html', context=context)

def Ladder(request):
    """View function for Leaderboard page of site."""

    context = {}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'ladder.html', context=context)

def WildCard(request):
    """View function for Leaderboard page of site."""
    week_values=[2,4,6,8]

    all_games = Game_Schedule.objects.all().filter(weekend='Wildcard')

    games_dict={}
    for g in all_games:

        # Make choice strings
        if g.dog==g.home:
            favorite=g.away
        else:
            favorite=g.home

        fav_str=favorite+'-'+str(g.spread)
        dog_str=g.dog+'+'+str(g.spread)
        print(fav_str,dog_str)

        games_dict[g]={'game_num':g.game_num,'home':g.home,'away':g.away,
        'spread':g.spread,'favstr':fav_str,'dogstr':dog_str}

    print(games_dict)
    context = {'games_dict': games_dict}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'wild_card_weekend.html', context=context)

def Division(request):
    """View function for Leaderboard page of site."""
    context = {}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'division_championship_weekend.html', context=context)

def Conference(request):
    """View function for Leaderboard page of site."""
    context = {}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'conference_championship_weekend.html', context=context)

def Superbowl(request):
    """View function for Leaderboard page of site."""
    context = {}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'superbowl_weekend.html', context=context)

def Picks(request):
    """View function for Leaderboard page of site."""
    # Do wildcard weekend to untangle

    all_games = Game_Schedule.objects.all()
    print(type(all_games),all_games)
    games_dict={}
    for g in all_games:
        print(g.game_num,g.home,g.away)
        games_dict[g]={'game_num':g.game_num,'home':g.home,'away':g.away,
        'dog':g.dog,'spread':g.spread}
        print('Game_num:',g.game_num)
    print(games_dict)

    context = {'games_dict': games_dict}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'wild_card_weekend_picks.html', context=context)

from django.views import generic

class Playoff_TeamListView(generic.ListView):
    model = Playoff_Team
