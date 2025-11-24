import os
from django.core.files.storage import DefaultStorage
from django.core.paginator import Paginator, EmptyPage
from django.template.response import TemplateResponse
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from filebrowser import signals
from filebrowser.sites import (
    FileBrowserSite,
    filebrowser_view,
    get_settings_var,
    get_breadcrumbs,
    admin_site,
)
from filebrowser.decorators import path_exists
from filebrowser.settings import (
    DEFAULT_SORTING_BY,
    DEFAULT_SORTING_ORDER,
    VERSIONS_BASEDIR,
)
from filebrowser.templatetags.fb_tags import query_helper


def media_matches(media_filter, obj):
    """Return True if `obj` satisfies the media-record filter.

    Supported values for media_filter:
    - 'has_record' -> keep objects where obj.has_media_record() is True
    - 'no_record'  -> keep objects where obj.has_media_record() is False
    If no media_filter is set, everything matches.
    """
    if not media_filter:
        return True
    try:
        has_attr = getattr(obj, "has_media_record", None)
        if callable(has_attr):
            has = bool(has_attr())
        else:
            has = bool(has_attr)
    except Exception:
        has = False
    if media_filter == "has_record":
        return has
    if media_filter == "no_record":
        return not has
    return True


class TekdbFileBrowserSite(FileBrowserSite):
    def files_folders_to_ignore(self):
        return ["__pycache__", "__init__.py", VERSIONS_BASEDIR]

    def get_urls(self):
        from django.urls import re_path

        urls = super().get_urls()

        urls += [
            re_path(
                r"^delete-media-without-record-confirm/",
                path_exists(
                    self, filebrowser_view(self.delete_media_without_record_confirm)
                ),
                name="fb_delete_all_media_without_record_confirm",
            ),
            re_path(
                r"^delete-media-without-record/",
                path_exists(self, filebrowser_view(self.delete_media_without_record)),
                name="fb_delete_all_media_without_record",
            ),
        ]
        return urls

    def browse(self, request):
        """Call upstream browse(), then apply server-side filtering for the
        `filter_media_record` query parameter. This keeps the UI filter backed
        by server logic without changing upstream code.
        """
        response = super().browse(request)

        # Only proceed if the TemplateResponse has context data we can
        # mutate.
        if not hasattr(response, "context_data"):
            return response

        media_filter = None
        try:
            media_filter = request.GET.get("filter_media_record")
        except Exception:
            media_filter = None

        paginator_replacements = {}

        # Walk context values and filter lists / paginators / pages
        for key, val in list(response.context_data.items()):
            try:
                # Page-like objects (have .paginator and .number)
                if (
                    hasattr(val, "paginator")
                    and hasattr(val, "number")
                    and key == "page"
                ):
                    orig_paginator = val.paginator
                    try:
                        full_list = list(orig_paginator.object_list)
                    except Exception:
                        full_list = list(getattr(val, "object_list", []))

                    filtered_full = [
                        o for o in full_list if media_matches(media_filter, o)
                    ]

                    per_page = getattr(settings, "FILEBROWSER_LIST_PER_PAGE", None)
                    if not per_page:
                        per_page = getattr(orig_paginator, "per_page", 10)

                    new_paginator = Paginator(filtered_full, per_page)
                    page_number = getattr(val, "number", 1)
                    try:
                        new_page = new_paginator.page(page_number)
                    except EmptyPage:
                        new_page = new_paginator.page(new_paginator.num_pages)

                    response.context_data[key] = new_page
                    paginator_replacements[orig_paginator] = new_paginator

            except Exception:
                # Non-fatal: skip entries we can't process
                pass

        # Replace any remaining references to original paginators with the
        # new ones so counts/num_pages are consistent.
        if paginator_replacements:
            for key, val in list(response.context_data.items()):
                for orig, new in list(paginator_replacements.items()):
                    if val is orig:
                        response.context_data[key] = new
                    elif hasattr(val, "paginator") and val.paginator is orig:
                        page_number = getattr(val, "number", 1)
                        try:
                            response.context_data[key] = new.page(page_number)
                        except EmptyPage:
                            response.context_data[key] = new.page(new.num_pages)

        # Update filelisting counts if present
        try:
            filelisting = response.context_data.get("filelisting")
            if filelisting is not None:
                # If filelisting exposes a list of current files, try to
                # update results_current/total conservatively.
                try:
                    # Some implementations keep a 'results_current' attr
                    # pointing at the currently visible files.
                    if hasattr(filelisting, "results_current"):
                        # Try to infer count from page/paginator if present
                        page = response.context_data.get(
                            "page"
                        ) or response.context_data.get("p")
                        if page is not None and hasattr(page, "object_list"):
                            filelisting.results_current = len(list(page.object_list))
                        else:
                            # Fallback: see if filelisting provides a total list
                            try:
                                filelisting.results_current = len(
                                    list(filelisting.files_listing_filtered())
                                )
                            except Exception:
                                pass
                    if hasattr(filelisting, "results_total"):
                        # If we can derive a total from a paginator replacement
                        p_new = None
                        for new in paginator_replacements.values():
                            p_new = new
                            break
                        if p_new is not None:
                            filelisting.results_total = getattr(
                                p_new, "count", len(getattr(p_new, "object_list", []))
                            )
                except Exception:
                    pass
        except Exception:
            pass

        return response

    def delete_media_without_record_confirm(self, request):
        """Confirm page to delete selected files that do not have associated media records."""

        query = request.GET
        path = "%s" % os.path.join(self.directory, query.get("dir", ""))

        filelisting = self.filelisting_class(
            path,
            filter_func=lambda fo: not fo.has_media_record()
            and fo.filename not in self.files_folders_to_ignore(),
            sorting_by=query.get("o", DEFAULT_SORTING_BY),
            sorting_order=query.get("ot", DEFAULT_SORTING_ORDER),
            site=self,
        )
        listings = filelisting.files_listing_filtered()

        return TemplateResponse(
            request,
            "filebrowser/delete_no_media_record_confirm.html",
            dict(
                admin_site.each_context(request),
                **{
                    "filelisting": listings,
                    "query": query,
                    "title": "Confirm Deletion of Unused Media Files",
                    "settings_var": get_settings_var(directory=self.directory),
                    "breadcrumbs": get_breadcrumbs(query, query.get("dir", "")),
                    "breadcrumbs_title": "Delete Unused Media Files",
                    "filebrowser_site": self,
                },
            ),
        )

    def delete_media_without_record(self, request):
        """Delete selected files that do not have associated media records."""
        query = request.GET
        path = "%s" % os.path.join(self.directory, query.get("dir", ""))

        filelisting = self.filelisting_class(
            path,
            filter_func=lambda fo: not fo.has_media_record()
            and fo.filename not in self.files_folders_to_ignore(),
            sorting_by=query.get("o", DEFAULT_SORTING_BY),
            sorting_order=query.get("ot", DEFAULT_SORTING_ORDER),
            site=self,
        )
        listing = filelisting.files_listing_filtered()

        deleted_files = []
        for fileobject in listing:
            try:
                signals.filebrowser_pre_delete.send(
                    sender=request,
                    path=fileobject.path,
                    name=fileobject.filename,
                    site=self,
                )
                # we have disabled versions for TEKDB,
                # but keep the call here in case that changes in future
                # or in the off chance versions exist
                fileobject.delete_versions()
                fileobject.delete()
                deleted_files.append(fileobject.filename)
                signals.filebrowser_post_delete.send(
                    sender=request,
                    path=fileobject.path,
                    name=fileobject.filename,
                    site=self,
                )
            except OSError:
                messages.add_message(
                    request,
                    messages.ERROR,
                    f"Error deleting file: {fileobject.filename}",
                )
                break

        messages.add_message(
            request, messages.SUCCESS, f"Deleted files: {', '.join(deleted_files)}"
        )

        # Redirect back to browse after deletion
        redirect_url = reverse(
            "filebrowser:fb_browse", current_app=self.name
        ) + query_helper(query, "", "filename,filetype")
        return HttpResponseRedirect(redirect_url)


storage = DefaultStorage()
site = TekdbFileBrowserSite(name="filebrowser", storage=storage)
site.directory = ""
