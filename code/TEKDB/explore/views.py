from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'page':'home',
        'pageTitle':'Welcome',
        'pageContent':"<p>Nullam pellentesque aliquet lectus vel ornare. Praesent lacus lorem, varius vitae metus et, euismod faucibus quam. Duis egestas consectetur magna at porta. Nulla massa nisl, scelerisque quis suscipit nec, vulputate quis neque. Vestibulum diam risus, feugiat a augue sollicitudin, sodales elementum velit. Nulla iaculis ligula id justo semper lobortis. In dapibus ultricies velit, id vestibulum libero lacinia eget. Sed in purus sed libero fringilla rutrum ut varius lectus. Aliquam lobortis imperdiet felis, at consequat tortor ultrices a.</p>",
        'user': request.user
    }
    return render(request, "welcome.html", context)

def about(request):
    context = {
        'page':'about',
        'pageTitle':'About',
        'pageContent':"<p>Proin eu semper libero. Vestibulum in massa nisi. Sed sed leo dolor. Praesent id arcu ornare, tincidunt velit eu, sodales orci. Nulla tincidunt velit nibh, laoreet ornare justo porttitor eu. Ut quam est, porta sed felis eu, viverra aliquam dolor. Curabitur nunc augue, elementum sed metus a, pellentesque vestibulum nisl. Phasellus nec ligula arcu. Duis eu scelerisque leo. Integer volutpat viverra neque at viverra. Etiam vitae sapien in eros porta feugiat in a.</p>",
        'user': request.user
    }
    return render(request, "tek_index.html", context)

def help(request):
    context = {
        'page':'help',
        'pageTitle':'Help',
        'pageContent':"<p>Morbi suscipit turpis in metus scelerisque accumsan. Curabitur consequat, erat sit amet rhoncus mattis, libero elit tincidunt dui, vel porta augue odio in diam. Morbi tincidunt ligula sem, in vestibulum lectus tincidunt porttitor. Phasellus cursus tortor libero, sit amet scelerisque erat aliquet quis. Aliquam egestas eros leo, eu commodo turpis iaculis id. Quisque consequat consequat nisi et semper. Donec commodo consectetur justo vel rhoncus. Praesent convallis tellus in aliquet dapibus. Nullam nisi lacus, euismod accumsan feugiat quis, placerat aliquet quam. Nulla sed euismod arcu, in commodo diam. Duis ac rhoncus ante, et dictum velit. Nunc sagittis lectus vel tortor sagittis interdum. Aliquam quis pulvinar purus. Mauris in efficitur tellus, dignissim porttitor risus.</p>",
        'user': request.user
    }
    return render(request, "tek_index.html", context)

def explore(request):
    context = {
        'page':'explore',
        'pageTitle':'Explore',
        'pageContent':"<p>In in mi vitae nibh posuere condimentum vitae eget quam. Etiam et urna id odio fringilla aliquet id hendrerit nisl. Ut sed ex vel felis rhoncus eleifend. Ut auctor facilisis vehicula. Ut sed dui nec ipsum pellentesque tempus.</p>",
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
                'description': "Proin varius sollicitudin nisi in pretium. Sed fringilla leo eget arcu facilisis posuere. Pellentesque aliquet venenatis ullamcorper. Duis ornare sem.",
                'link': '/explore/place/1',
            },{
                'id': 1,
                'type': 'resource',
                'name': 'Resource 1',
                'image': '/static/explore/img/demo-resource.png',
                'description': "Suspendisse tincidunt orci sed metus lobortis eleifend. Aliquam vel volutpat augue. Class aptent taciti sociosqu ad litora torquent per conubia.",
                'link': '/explore/resource/1',
            },{
                'id': 1,
                'type': 'activity',
                'name': 'Activity 1',
                'image': '/static/explore/img/demo-activity.png',
                'description': "Nulla maximus vitae urna eget dapibus. Donec id varius nulla, non elementum sem. Sed nec dapibus metus. Proin sit amet.",
                'link': '/explore/activity/1',
            },{
                'id': 1,
                'type': 'citation',
                'name': 'Citation 1',
                'image': '/static/explore/img/demo-citation.png',
                'description': "Quisque egestas mi lorem, at vehicula sem congue nec. Integer dui sapien, pellentesque eu auctor eget, laoreet sed nisi. Nunc.",
                'link': '/explore/citatation/1',
            },{
                'id': 1,
                'type': 'media',
                'name': 'Media 1',
                'image': '/static/explore/img/demo-media.png',
                'description': "Maecenas scelerisque molestie nisl, ac blandit ipsum sagittis et. Donec ut enim pulvinar, suscipit lacus a, venenatis mauris. Aenean interdum.",
                'link': '/explore/media/1',
            },
        ]
    }
    return JsonResponse(results)
