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
        'places': [tekmodels.Places],
        'locality': [tekmodels.Locality],
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
        return sum([searchable_models[key] for key in ['resources','places', 'citations', 'media', 'activities']],[])
    else:
        return []

def get_by_model_type(request, model_type):
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
    import json
    import TEKDB
    all_categories = ['places','resources','activities','citations','media']
    if request.method == 'POST':
        query_string=request.POST['query']
        if 'category' in request.POST.keys():
            categories = [request.POST['category']]
        else:
            keys = request.POST.keys()
            categories = []
            if 'places' in keys and request.POST['places'] :
                categories.append('places')
            if 'resources' in keys and request.POST['resources']:
                categories.append('resources')
            if 'activities' in keys and request.POST['activities']:
                categories.append('activities')
            if 'citations' in keys and request.POST['citations']:
                categories.append('citations')
            if 'media' in keys and request.POST['media']:
                categories.append('media')
    else:
        if 'query' in request.GET.keys():
            query_string = request.GET.get('query')
        else:
            query_string = None
        if 'category' in request.GET.keys():
            categories = [request.GET.get('category')]
        else:
            categories = ['all']

    if categories == ['all']:
        categories = all_categories

    category_checkboxes = ''
    for category in all_categories:
        if category in categories:
            checked = ' checked=true'
        else:
            checked = ''
        category_checkboxes = '%s<input type="checkbox" name="%s" value="%s"%s>%s<br>\n' % (category_checkboxes, category, category,checked,category.capitalize())

    if query_string in [None, '', '*']:
        query_string_visible = 'No keyword search specified.'
    else:
        query_string_visible = query_string

    if query_string not in [None, '', '*']:
        query_value = ' value=%s' % query_string
    else:
        query_value = ''
    keyword_search_input = '<label for="search-text">Search Phrase</label><input type="text" class="form-control" id="search-text" name="query" placeholder="Search Phrase"%s>' % query_value

    context = {
        'query': query_string,
        'keyword': query_string_visible,
        'keyword_search_input': keyword_search_input,
        'categories': json.dumps(categories),
        'category_checkboxes': category_checkboxes,
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
        categories = [request.GET.get('category')]
    else:
        categories = []
        if 'places' in request.GET.keys() and request.GET['places']:
            categories.append('places')
        if 'resources' in request.GET.keys() and request.GET['resources']:
            categories.append('resources')
        if 'activities' in request.GET.keys() and request.GET['activities']:
            categories.append('activities')
        if 'citations' in request.GET.keys() and request.GET['citations']:
            categories.append('citations')
        if 'media' in request.GET.keys() and request.GET['media']:
            categories.append('media')
    #TODO: need to handle #results/page, page#

    resultlist = []
    #TODO: Loop through list of categories
    for category in categories:
        query_models = get_model_by_type(category)
        for model in query_models:
            # Find all results matching keyword in this model
            model_results = model.keyword_search(keyword_string)
            for result in model_results:
                # Create JSON object to be resturned
                resultlist.append(result.get_response_format())

    results = {
        'resultList' : resultlist
    }

    return JsonResponse(results)
