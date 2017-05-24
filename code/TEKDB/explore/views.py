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

def get_model_by_type(model_type):
    from TEKDB import models as tekmodels
    searchable_models = {
        'resource': [tekmodels.Resources],
        'place': [tekmodels.Places],
        'locality': [tekmodels.Locality],
        'citation': [tekmodels.Citations],
        'media': [tekmodels.Media],
        'event': [
            tekmodels.Localityplaceresourceevent,
            tekmodels.Mediacitationevents,
            tekmodels.Placescitationevents,
            tekmodels.Placesmediaevents,
            tekmodels.Placesresourcecitationevents,
            tekmodels.Placesresourceevents,
            tekmodels.Placesresourcemediaevents,
            tekmodels.Resourceactivitycitationevents,
            tekmodels.Resourceactivitymediaevents,
            tekmodels.Resourceresourceevents,
            tekmodels.Resourcesactivityevents,
            tekmodels.Resourcescitationevents,
            tekmodels.Resourcesmediaevents,
        ],
        'Localityplaceresourceevent': [tekmodels.Localityplaceresourceevent],
        'Mediacitationevents': [tekmodels.Mediacitationevents],
        'Placescitationevents': [tekmodels.Placescitationevents],
        'Placesmediaevents': [tekmodels.Placesmediaevents],
        'Placesresourcecitationevents': [tekmodels.Placesresourcecitationevents],
        'Placesresourceevents': [tekmodels.Placesresourceevents],
        'Placesresourcemediaevents': [tekmodels.Placesresourcemediaevents],
        'Resourceactivitycitationevents': [tekmodels.Resourceactivitycitationevents],
        'Resourceactivitymediaevents': [tekmodels.Resourceactivitymediaevents],
        'Resourceresourceevents': [tekmodels.Resourceresourceevents],
        'Resourcesactivityevents': [tekmodels.Resourcesactivityevents],
        'Resourcescitationevents': [tekmodels.Resourcescitationevents],
        'Resourcesmediaevents': [tekmodels.Resourcesmediaevents],
    }

    if model_type in searchable_models.keys():
        return searchable_models[model_type]
    elif model_type == 'all':
        return sum([searchable_models[key] for key in ['resource','place','locality','citation', 'media']],[])
    else:
        return []

def get_by_model_type(request, model_type):
    ### Note: This would be better left done by the normal 'query' process
    # models = get_model_by_type(model_type)
    # return_values = []
    # for model in models:
    #     for obj in model.objects.all():
    #         return_values.push(obj.get_query_json())
    context = {
        'query': '',
        'category': model_type,
        'page':'Results',
        'pageTitle':'Results',
        'pageContent':"<p>Your search results:</p>",
        'user': request.user
    }
    return render(request, "results.html", context)

def get_by_model_id(request, model_type, id):
    models = get_model_by_type(model_type)
    if len(models) == 1:
        try:
            model = models[0]
            obj = model.objects.get(pk=id)
            record_json = obj.get_query_json()
        except Exception as e:
            obj = None
            record_json = {}
    else:
        obj = None
        record_json = {}

    context = {
        'page':'Record',
        'pageTitle':'Record',
        'pageContent':"<p>Your record:</p>",
        'record': record_json,
        'user': request.user
    }
    return render(request, "record.html", context)


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
        'query': query_string,
        'category': category,
        'page':'Results',
        'pageTitle':'Results',
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

    ### Use ipdb to dig into your code while it runs:
    # import ipdb
    # ipdb.set_trace()
    ### n to step to _N_ext line of code
    ### c to let the code _C_ontinue
    ### Otherwise just write python in as you would in the django shell or in this filter
    ###
    #TODO: Get list of models to query (get_model_by_type)
    #TODO: Loop through models, querying each as needed, collecting responses into 'resultlist'

    #import your model
    from TEKDB.models import Resources
    #Check for 'wildcard' (match everything) search
    if not keyword_string in ['*', '']:
        #filter on appropriate fields (may be best to let the model figure this out for itself)
        #TODO: make query case-insensitive and less strict (see doc on '__icontains')
        query_results = Resources.objects.filter(commonname=keyword_string)
    else:
        #If search is a wildcard, grab everything
        query_results = Resources.objects.all()

    #Create empty list to fill
    resultlist = []
    #Loop over all results
    for resource in query_results:
        # add formatted result to resultlist (may be best to have model format itself)
        resultlist.append({
            'id': resource.pk,
            # pk is django keyword for any model's Primary Key
            'type': 'resources',
            'name': resource.commonname,
            'image': '/static/explore/img/demo-resource.png',
            'description': resource.indigenousname,
            'link': '/explore/resource/%d' % resource.pk,
        })
    # Create JSON object to be resturned
    results = {
        'resultList' : resultlist
    }

    #####################################
    ### START PLACEHOLDER FOR TESTING ###
    #####################################
    # from copy import deepcopy
    # results = deepcopy(TEKDB.settings.TEST_QUERY_RESULTS)
    # if category and not category == 'all':
    #     results['resultList'] = [ x for x in results['resultList'] if x['type'] == category]
    # if keyword_string and not keyword_string == '':
    #     results['resultList'] = [ x for x in results['resultList'] if keyword_string.lower() in " ".join([x['type'],x['name'],x['description']]).lower()]
    ###################################
    ### END PLACEHOLDER FOR TESTING ###
    ###################################

    return JsonResponse(results)
