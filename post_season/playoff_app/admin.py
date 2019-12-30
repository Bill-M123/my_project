from django.contrib import admin

# Register your models here.
from .models import Weekly_Picks, Ladder_Picks

admin.site.register(Weekly_Picks)
admin.site.register(Ladder_Picks)
