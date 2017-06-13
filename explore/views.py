from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    try:
        page_content_obj = PageContent.objects.get(page="Welcome")
        if page_content_obj.is_html:
            page_content = page_content_obj.html_content
        else:
            page_content = page_content_obj.content
    except Exception as e:
        page_content = "<h1>Welcome</h1><h3>Set Welcome Page Content In Admin</h3>"

    context = {
        'page':'home',
        'pageTitle':'Welcome',
        'pageContent':page_content,
        'user': request.user
    }
    return render(request, "welcome.html", context)

def about(request):
    try:
        page_content_obj = PageContent.objects.get(page="About")
        if page_content_obj.is_html:
            page_content = page_content_obj.html_content
        else:
            page_content = page_content_obj.content
    except Exception as e:
        page_content = "<h1>About</h1><h3>Set About Page Content In Admin</h3>"
    context = {
        'page':'about',
        'pageTitle':False,
        'pageContent':page_content,
        'user': request.user
    }
    return render(request, "tek_index.html", context)

def help(request):
    try:
        page_content_obj = PageContent.objects.get(page="Help")
        if page_content_obj.is_html:
            page_content = page_content_obj.html_content
        else:
            page_content = page_content_obj.content
    except Exception as e:
        page_content = "<h1>Help</h1><h3>Set Help Page Content In Admin</h3>"
    context = {
        'page':'help',
        'pageTitle':False,
        'pageContent':page_content,
        'user': request.user
    }
    return render(request, "tek_index.html", context)

def explore(request):
    if not request.user.is_authenticated:
        return home(request)
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
        'resources': [tekmodels.Resources],
        'places': [tekmodels.Places, tekmodels.Locality],
        # 'locality': [tekmodels.Locality],
        'citations': [tekmodels.Citations],
        'media': [tekmodels.Media],
        'activities': [tekmodels.ResourcesActivityEvents],
        'relationships': [
            tekmodels.LocalityPlaceResourceEvent,
            tekmodels.MediaCitationEvents,
            tekmodels.PlacesCitationEvents,
            tekmodels.PlacesMediaEvents,
            tekmodels.PlacesResourceCitationEvents,
            tekmodels.PlacesResourceEvents,
            tekmodels.PlacesResourceMediaEvents,
            tekmodels.ResourceActivityCitationEvents,
            tekmodels.ResourceActivityMediaEvents,
            tekmodels.ResourceResourceEvents,
            tekmodels.ResourcesActivityEvents,
            tekmodels.ResourcesCitationEvents,
            tekmodels.ResourcesMediaEvents,
        ],
        'Localityplaceresourceevents': [tekmodels.LocalityPlaceResourceEvent],
        'Mediacitationevents': [tekmodels.MediaCitationEvents],
        'Placescitationevents': [tekmodels.PlacesCitationEvents],
        'Placesmediaevents': [tekmodels.PlacesMediaEvents],
        'Placesresourcecitationevents': [tekmodels.PlacesResourceCitationEvents],
        'Placesresourceevents': [tekmodels.PlacesResourceEvents],
        'Placesresourcemediaevents': [tekmodels.PlacesResourceMediaEvents],
        'Resourceactivitycitationevents': [tekmodels.ResourceActivityCitationEvents],
        'Resourceactivitymediaevents': [tekmodels.ResourceActivityMediaEvents],
        'Resourceresourceevents': [tekmodels.ResourceResourceEvents],
        'Resourcesactivityevents': [tekmodels.ResourcesActivityEvents],
        'Resourcescitationevents': [tekmodels.ResourcesCitationEvents],
        'Resourcesmediaevents': [tekmodels.ResourcesMediaEvents],
    }

    if model_type in searchable_models.keys():
        return searchable_models[model_type]
    elif model_type == 'all':
        return sum([searchable_models[key] for key in ['resources','places', 'citations', 'media', 'activities', 'relationships']],[])
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

    resultlist = []
    query_models = get_model_by_type(category)
    for model in query_models:
        # Find all results matching keyword in this model
        model_results = model.keyword_search(keyword_string)
        for result in model_results:
            # Create JSON object to be resturned
            resultlist.append(result.get_response_format())

    # resultlist.append({
    #     'id': resource.pk,
    #     # pk is django keyword for any model's Primary Key
    #     'type': 'resources',
    #     'name': resource.commonname,
    #     'image': '/static/explore/img/demo-resource.png',
    #     'description': resource.indigenousname,
    #     'link': '/explore/resource/%d' % resource.pk,
    # })
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
