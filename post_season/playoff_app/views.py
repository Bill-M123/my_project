from django.shortcuts import render

from playoff_app.models import Playoff_Team, Weekly_Pick, Ladder_Pick

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
    context = {}
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

from django.views import generic

class Playoff_TeamListView(generic.ListView):
    model = Playoff_Team
