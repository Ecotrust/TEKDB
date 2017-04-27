from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'page':'home',
        'pageTitle':'Welcome',
        'pageContent':"<p>Earl Grey tea, watercress sandwiches... and Bularian canapés? Are you up for promotion? That might've been one of the shortest assignments in the history of Starfleet. Is it my imagination, or have tempers become a little frayed on the ship lately? The Enterprise computer system is controlled by three primary main processor cores, cross-linked with a redundant melacortz ramistat, fourteen kiloquad interface modules. I guess it's better to be lucky than good. Then maybe you should consider this: if anything happens to them, Starfleet is going to want a full investigation.</p>"
    }
    return render(request, "welcome.html", context)

def about(request):
    context = {
        'page':'about',
        'pageTitle':'About',
        'pageContent':"<p>This should be interesting. When has justice ever been as simple as a rule book? Now, how the hell do we defeat an enemy that knows us better than we know ourselves? The game's not big enough unless it scares you a little. What's a knock-out like you doing in a computer-generated gin joint like this? Talk about going nowhere fast. We have a saboteur aboard.</p>",
    }
    return render(request, "tek_index.html", context)

def help(request):
    context = {
        'page':'help',
        'pageTitle':'Help',
        'pageContent':"<p>I am your worst nightmare! A surprise party? Mr. Worf, I hate surprise parties. I would *never* do that to you. Computer, belay that order. Your shields were failing, sir. I'll alert the crew. Fear is the true enemy, the only enemy. Talk about going nowhere fast. I think you've let your personal feelings cloud your judgement. I'd like to think that I haven't changed those things, sir. I suggest you drop it, Mr. Data.</p>",
    }
    return render(request, "tek_index.html", context)

def explore(request):
    context = {
        'page':'explore',
        'pageTitle':'Explore',
        'pageContent':"<p>I suggest you drop it, Mr. Data. Mr. Worf, you sound like a man who's asking his friend if he can start dating his sister. We have a saboteur aboard. Wait a minute - you've been declared dead. You can't give orders around here. When has justice ever been as simple as a rule book? What? We're not at all alike! This should be interesting. and attack the Romulans. I will obey your orders. I will serve this ship as First Officer. And in an attack against the Enterprise, I will die with this crew. But I will not break my oath of loyalty to Starfleet.</p>",
    }
    return render(request, "tek_index.html", context)
