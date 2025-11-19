from django.core.files.storage import DefaultStorage
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings
from filebrowser.sites import FileBrowserSite


class FilesOnlyFileBrowserSite(FileBrowserSite):
    def browse(self, request):
        response = super().browse(request)

        # if hasattr(response, 'context_data'):
        #     paginator_replacements = {}

        #     for key, val in list(response.context_data.items()):
        #         try:
        #             # If this is a paginated Page-like object, rebuild the
        #             # paginator using the filtered full object list.
        #             if hasattr(val, 'paginator') and hasattr(val, 'number'):
        #                 orig_paginator = val.paginator
        #                 try:
        #                     full_list = list(orig_paginator.object_list)
        #                 except Exception:
        #                     full_list = list(getattr(val, 'object_list', []))

        #                 # don't show folders or .py files
        #                 # TODO: is this ok? 
        #                 filtered_full = [o for o in full_list if not getattr(o, 'is_folder', False) and not str(o).endswith('.py')]

        #                 # Recreate paginator and select the same page number if possible
        #                 # Prefer the explicit FILEBROWSER_LIST_PER_PAGE setting
        #                 # if the project defines it. Otherwise fall back to the
        #                 # original paginator's per_page value, then to 20.
        #                 per_page = getattr(settings, 'FILEBROWSER_LIST_PER_PAGE', None)
        #                 if not per_page:
        #                     per_page = getattr(orig_paginator, 'per_page', 20)
        #                 new_paginator = Paginator(filtered_full, per_page)
        #                 page_number = getattr(val, 'number', 1)
        #                 try:
        #                     new_page = new_paginator.page(page_number)
        #                 except EmptyPage:
        #                     # If requested page is out of range after filtering,
        #                     # return the last page instead.
        #                     new_page = new_paginator.page(new_paginator.num_pages)

        #                 # Replace this page in the context and remember the
        #                 # paginator mapping so other context keys can be
        #                 # updated too.
        #                 response.context_data[key] = new_page
        #                 paginator_replacements[orig_paginator] = new_paginator

        #             # Plain lists/tuples (e.g. 'folders')
        #             elif isinstance(val, (list, tuple)):
        #                 response.context_data[key] = [o for o in val if not getattr(o, 'is_folder', False)]
        #         except Exception:
        #             # On any unexpected structure, skip and leave it unchanged
        #             pass
                
            
        #         for new in list(paginator_replacements.values()):
        #             print(new)
        #             new_count = getattr(new, 'count', None)
        #             print(new_count)
        #             if new_count is None:
        #                 # Fallback to len of object_list if paginator doesn't
        #                 # expose count (shouldn't happen with Django Paginator)
        #                 new_count = len(getattr(new, 'object_list', []))

        #             for value in list(response.context_data.values()):
        #                 try:
        #                     if hasattr(value, 'results_total'):
        #                         setattr(value, 'results_total', new_count)

        #                 except Exception:
        #                     # Non-critical; skip any objects we can't mutate
        #                     pass
        
        return response

# Create your custom site instance
storage = DefaultStorage()
site = FilesOnlyFileBrowserSite(name='filebrowser', storage=storage)
site.directory = ""
