from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'page':'home',
        'pageTitle':'Welcome',
        'pageContent':"<p>Earl Grey tea, watercress sandwiches... and Bularian canapes? Are you up for promotion? That might've been one of the shortest assignments in the history of Starfleet. Is it my imagination, or have tempers become a little frayed on the ship lately? The Enterprise computer system is controlled by three primary main processor cores, cross-linked with a redundant melacortz ramistat, fourteen kiloquad interface modules. I guess it's better to be lucky than good. Then maybe you should consider this: if anything happens to them, Starfleet is going to want a full investigation.</p>",
        'user': request.user
    }
    return render(request, "welcome.html", context)

def about(request):
    context = {
        'page':'about',
        'pageTitle':'About',
        'pageContent':"<p>This should be interesting. When has justice ever been as simple as a rule book? Now, how the hell do we defeat an enemy that knows us better than we know ourselves? The game's not big enough unless it scares you a little. What's a knock-out like you doing in a computer-generated gin joint like this? Talk about going nowhere fast. We have a saboteur aboard.</p>",
        'user': request.user
    }
    return render(request, "tek_index.html", context)

def help(request):
    context = {
        'page':'help',
        'pageTitle':'Help',
        'pageContent':"<p>I am your worst nightmare! A surprise party? Mr. Worf, I hate surprise parties. I would *never* do that to you. Computer, belay that order. Your shields were failing, sir. I'll alert the crew. Fear is the true enemy, the only enemy. Talk about going nowhere fast. I think you've let your personal feelings cloud your judgement. I'd like to think that I haven't changed those things, sir. I suggest you drop it, Mr. Data.</p>",
        'user': request.user
    }
    return render(request, "tek_index.html", context)

def explore(request):
    context = {
        'page':'explore',
        'pageTitle':'Explore',
        'pageContent':"<p>I suggest you drop it, Mr. Data. Mr. Worf, you sound like a man who's asking his friend if he can start dating his sister. We have a saboteur aboard. Wait a minute - you've been declared dead. You can't give orders around here. When has justice ever been as simple as a rule book? What? We're not at all alike! This should be interesting. and attack the Romulans. I will obey your orders. I will serve this ship as First Officer. And in an attack against the Enterprise, I will die with this crew. But I will not break my oath of loyalty to Starfleet.</p>",
        'user': request.user
    }
    return render(request, "explore.html", context)

def search(request):
    # if request.method == 'GET':
    #     return explore(request)
    # else:
    if request.method == 'POST':
        query_string=request.POST['query']
        category = request.POST['category']
    else:
        if 'query' in request.GET.keys():
            query_string = request.GET.get('query')
        else:
            query_string = None
        if 'category' in request.GET.keys():
            category = request.GET.get('category')
        else:
            category = '*'
    context = {
        'query': query,
        'category': category,
        'page':'explore',
        'pageTitle':'Explore',
        'pageContent':"<p>Your search results:</p>",
        'user': request.user
    }
    return render(request, "results.html", context)

def query(request):
    from django.http import JsonResponse
    import TEKDB
    if 'query' in request.GET.keys():
        keyword_string = str(request.GET.get('query'))
    else:
        keyword_string = None
    if 'category' in request.GET.keys() and request.GET.get('category') in TEKDB.settings.SEARCH_CATEGORIES:
        category = request.GET.get('category')
    else:
        category = None

    #TODO: Query database to generate 'results' dict.
    results = {
        'resultList' :[
            {
                'id': 1,
                'type': 'place',
                'name': 'Location 1',
                'image': '/static/explore/img/demo-map.png',
                'description': "Could someone survive inside a transporter buffer for 75 years? Fate. It protects fools, little children, and ships named \"Enterprise.\" Wouldn't that bring about chaos? That might've been one of the shortest assignments in the history of Starfleet. We have a saboteur aboard.",
                'link': '/explore/place/1',
            },{
                'id': 1,
                'type': 'resource',
                'name': 'Resource 1',
                'image': '/static/explore/img/demo-resource.png',
                'description': "I'd like to think that I haven't changed those things, sir. Computer, lights up! But the probability of making a six is no greater than that of rolling a seven.",
                'link': '/explore/resource/1',
            },{
                'id': 1,
                'type': 'activity',
                'name': 'Activity 1',
                'image': '/static/explore/img/demo-activity.png',
                'description': "Damage report! Fear is the true enemy, the only enemy. Shields up! Rrrrred alert! Your shields were failing, sir.",
                'link': '/explore/activity/1',
            },{
                'id': 1,
                'type': 'citation',
                'name': 'Citation 1',
                'image': '/static/explore/img/demo-citation.png',
                'description': "Talk about going nowhere fast. But the probability of making a six is no greater than that of rolling a seven. The Federation's gone; the Borg is everywhere! Yes, absolutely, I do indeed concur, wholeheartedly!",
                'link': '/explore/citatation/1',
            },{
                'id': 1,
                'type': 'media',
                'name': 'Media 1',
                'image': '/static/explore/img/demo-media.png',
                'description': "I've had twelve years to think about it. And if I had it to do over again, I would have grabbed the phaser and pointed it at you instead of them. Besides, you look good in a dress. I recommend you don't fire until you're within 40,000 kilometers. The look in your eyes, I recognize it. You used to have it for me.",
                'link': '/explore/media/1',
            },
        ]
    }
    return JsonResponse(results)
