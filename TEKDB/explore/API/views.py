from django.http import Http404, HttpResponse
from django.middleware.csrf import get_token
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView

from .serializers import PageContentSerializer, SiteConfigurationSerializer
from ..models import PageContent


class PageContentViewSet(viewsets.ModelViewSet):
    """
    CRUD for PageContent via DRF.
    """

    serializer_class = PageContentSerializer
    queryset = PageContent.objects.all()
    permission_classes = [permissions.AllowAny]


class SiteConfigurationAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        from ..context_processors import explore_context

        # Get configuration data from context processor
        config_data = explore_context(request)

        serializer = SiteConfigurationSerializer(config_data)
        return Response(serializer.data)


class CsrfTokenAPIView(APIView):
    """
    Return CSRF token for the client to use in subsequent requests.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        csrf_token = get_token(request)
        response = Response({"csrfToken": csrf_token})
        # Ensure the CSRF cookie is set in the response
        response.set_cookie(
            key="csrftoken",
            value=csrf_token,
            max_age=86400,  # 1 day
            httponly=False,  # Allow JavaScript to read it
            samesite="Lax",
        )
        return response


# ----- Utility functions ported from template views -----
def _get_project_geography():
    from TEKDB.settings import DATABASE_GEOGRAPHY

    return DATABASE_GEOGRAPHY


def _get_model_by_type(model_type):
    from TEKDB import models as tekmodels

    searchable_models = {
        "resources": [tekmodels.Resources],
        "places": [tekmodels.Places],
        "locality": [tekmodels.Locality],
        "sources": [tekmodels.Citations],
        "citations": [tekmodels.Citations],
        "media": [tekmodels.Media],
        "activities": [tekmodels.ResourcesActivityEvents],
        "relationships": [
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
            tekmodels.ResourcesCitationEvents,
            tekmodels.ResourcesMediaEvents,
        ],
        "localityplaceresourceevents": [tekmodels.LocalityPlaceResourceEvent],
        "mediacitationevents": [tekmodels.MediaCitationEvents],
        "placescitationevents": [tekmodels.PlacesCitationEvents],
        "placesmediaevents": [tekmodels.PlacesMediaEvents],
        "placesresourcecitationevents": [tekmodels.PlacesResourceCitationEvents],
        "placesresourceevents": [tekmodels.PlacesResourceEvents],
        "placesresourcemediaevents": [tekmodels.PlacesResourceMediaEvents],
        "resourceactivitycitationevents": [tekmodels.ResourceActivityCitationEvents],
        "resourceactivitymediaevents": [tekmodels.ResourceActivityMediaEvents],
        "resourceresourceevents": [tekmodels.ResourceResourceEvents],
        "resourcesactivityevents": [tekmodels.ResourcesActivityEvents],
        "resourcescitationevents": [tekmodels.ResourcesCitationEvents],
        "resourcesmediaevents": [tekmodels.ResourcesMediaEvents],
        "people": [tekmodels.People],
    }

    if model_type.lower() in searchable_models.keys():
        return searchable_models[model_type.lower()]
    elif model_type.lower() == "all":
        return sum(
            [
                searchable_models[key]
                for key in ["resources", "places", "sources", "media", "activities"]
            ],
            [],
        )
    else:
        return []


# ----- Page content endpoints -----
class PageContentSingle(APIView):
    """Return single page content by name (Home/About/Help)."""

    permission_classes = [permissions.AllowAny]

    def get(self, request, name: str):
        try:
            page_content_obj = PageContent.objects.get(page=name)
            page_content = (
                page_content_obj.html_content
                if page_content_obj.is_html
                else page_content_obj.content
            )
        except Exception:
            page_content = f"<h1>{name}</h1><h3>Set {name} Page Content In Admin</h3>"

        return Response(
            {
                "page": name.lower(),
                "pageTitle": name,
                "pageContent": page_content,
            }
        )


class ExploreByType(APIView):
    """Explore for a specific model type."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, model_type):
        return Response(
            {
                "query": "",
                "category": model_type,
                "page": "Results",
                "pageTitle": "Results",
                "pageContent": "<p>Your search results:</p>",
                "user": str(request.user),
            }
        )


# ----- Explore/search endpoints -----
class ExploreSearch(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_verbose_field_name(self, model, field_path):
        parts = field_path.split("__")
        field = None
        current_model = model
        for part in parts:
            field = current_model._meta.get_field(part)
            if hasattr(field, "related_model") and field.related_model:
                current_model = field.related_model
        return (
            field.verbose_name.title()
            if field
            else field_path.replace("_", " ").title()
        )

    def remove_match_prefix(self, string):
        if string and string.startswith("match_"):
            return string[6:]
        return string

    def find_match_attributes(self, obj):
        return [attr for attr in dir(obj) if "match" in attr]

    def get_greatest_similarity_attribute(self, result, pks):
        greatest_similarity_attribute = None
        matching_attributes = []
        for match_attr in self.find_match_attributes(result):
            match_value = getattr(result, match_attr)
            if match_value is not None and match_value == result.similarity:
                matching_attributes.append(match_attr)
        if len(matching_attributes) == 1:
            greatest_similarity_attribute = matching_attributes[0]
        elif len(matching_attributes) > 0:
            num_same_id = pks.get(result.pk, 1)
            if num_same_id - 1 < len(matching_attributes):
                greatest_similarity_attribute = matching_attributes[num_same_id - 1]
                pks[result.pk] = max(0, num_same_id - 1)
            else:
                greatest_similarity_attribute = matching_attributes[0]
        return greatest_similarity_attribute

    def get_results(self, keyword_string, categories):
        if keyword_string is None:
            keyword_string = ""
        resultlist = []
        for category in categories:
            query_models = _get_model_by_type(category)
            for model in query_models:
                model_results = model.keyword_search(keyword_string)
                pks = {}
                for result in model_results:
                    if hasattr(result, "pk"):
                        pks[result.pk] = pks.get(result.pk, 0) + 1
                for result in model_results:
                    greatest_attr = self.get_greatest_similarity_attribute(result, pks)
                    actual_attribute = (
                        self.remove_match_prefix(greatest_attr)
                        if greatest_attr
                        else None
                    )
                    verbose_name = (
                        self.get_verbose_field_name(model, actual_attribute)
                        if actual_attribute
                        else None
                    )
                    headline_key = (
                        f"headline_{actual_attribute}" if actual_attribute else None
                    )
                    headline_value = (
                        getattr(result, headline_key)
                        if headline_key and hasattr(result, headline_key)
                        else None
                    )
                    result_json = result.get_response_format()
                    if keyword_string != "":
                        result_json["rank"] = result.rank
                        result_json["similarity"] = result.similarity
                        result_json["headline"] = (
                            f"<p class='headline'>{verbose_name}: {headline_value}</p>"
                            if headline_value and verbose_name
                            else None
                        )
                    else:
                        result_json["rank"] = 0
                        result_json["similarity"] = 0
                        result_json["headline"] = None
                    resultlist.append(result_json)
        return sorted(
            resultlist, key=lambda res: (res["rank"], res["similarity"]), reverse=True
        )

    def get(self, request):
        all_categories = ["places", "resources", "activities", "sources", "media"]
        query_string = request.GET.get("query")
        categories = (
            request.GET.getlist("category") or [request.GET.get("category")]
            if request.GET.get("category")
            else []
        )
        if categories == []:
            # derive from flags or default to all
            for key in all_categories:
                if request.GET.get(key) == "true":
                    categories.append(key)
            if categories == []:
                categories = ["all"]
        # sanitize categories
        # Zero tolerance for mispelled or 'all' categories. if it's not perfect, fail to 'all'
        for category in categories:
            if category not in all_categories:
                categories = all_categories
                break
        results = self.get_results(query_string, categories)

        # cap results by config
        try:
            from configuration.models import Configuration

            max_results = Configuration.objects.all()[0].max_results_returned
        except Exception:
            from TEKDB.settings import DEFAULT_MAXIMUM_RESULTS

            max_results = DEFAULT_MAXIMUM_RESULTS

        too_many = len(results) > max_results
        if too_many:
            results = results[:max_results]

        geo = _get_project_geography()
        return Response(
            {
                "results": results,
                "categories": categories,
                "query": query_string,
                "too_many_results": too_many,
                "map": {
                    "default_lon": geo["default_lon"],
                    "default_lat": geo["default_lat"],
                    "default_zoom": geo["default_zoom"],
                    "min_zoom": geo["min_zoom"],
                    "max_zoom": geo["max_zoom"],
                    "extent": geo["map_extent"],
                },
            }
        )


class ExploreById(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, model_type, id):
        models = _get_model_by_type(model_type)
        if len(models) != 1:
            return Response(
                {"error": f"Incorrect number of models for {model_type}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        model = models[0]
        try:
            obj = model.objects.get(pk=int(id))
            record_dict = obj.get_record_dict(request.user, 3857)
        except Exception:
            raise Http404
        geo_info_needed = False
        if ("map" in record_dict and record_dict["map"] is not None) or any(
            rel.get("key") == "Place-Resource Events"
            and any((val.get("map") is not None) for val in rel.get("value", []))
            for rel in record_dict.get("relationships", [])
        ):
            geo_info_needed = True

        payload = {"record": record_dict, "model": model_type, "id": id}
        if geo_info_needed:
            geo = _get_project_geography()
            payload["map"] = {
                "default_lon": geo["default_lon"],
                "default_lat": geo["default_lat"],
                "default_zoom": geo["default_zoom"],
                "min_zoom": geo["min_zoom"],
                "max_zoom": geo["max_zoom"],
                "extent": geo["map_extent"],
            }
        return Response(payload)


class ExportRecord(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, model_type, id, format):
        models = _get_model_by_type(model_type)
        if len(models) != 1:
            return Response(
                {"error": f"Incorrect number of models for {model_type}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        model = models[0]
        try:
            obj = model.objects.get(pk=id)
            record_dict = obj.get_record_dict(request.user, 4326)
        except Exception as e:
            return Response(
                {"error": "unknown error", "code": f"{e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        filename = f"{model_type}_{id}_{record_dict.get('name', 'record')}"
        if format == "xls":
            # XLSX export
            import io
            from xlsxwriter.workbook import Workbook

            output = io.BytesIO()
            workbook = Workbook(output, {"in_membory": True})
            worksheet = workbook.add_worksheet()
            workbook.add_format({"bold": True})
            row = 0

            # helper for ordered keys
            def get_sorted_keys(keys):
                ordered = []
                for key in [
                    "name",
                    "image",
                    "subtitle",
                    "data",
                    "relationships",
                    "map",
                    "link",
                    "enteredbyname",
                    "enteredbydate",
                    "modifiedbyname",
                    "modifiedbydate",
                ]:
                    if key in keys:
                        keys.remove(key)
                        ordered.append(key)
                return ordered + keys

            for key in get_sorted_keys(list(record_dict.keys())):
                field = record_dict[key]
                if (
                    isinstance(field, list)
                    and len(field) > 0
                    and isinstance(field[0], dict)
                ):
                    for item in field:
                        if "key" in item and "value" in item and len(item.keys()) == 2:
                            if (
                                isinstance(item["value"], list)
                                and len(item["value"]) > 0
                            ):
                                for sub_item in item["value"]:
                                    worksheet.write(row, 0, f"{key} - {item['key']}")
                                    worksheet.write(
                                        row, 1, sub_item.get("name", str(sub_item))
                                    )
                                    row += 1
                            else:
                                worksheet.write(row, 0, f"{key} - {item['key']}")
                                try:
                                    worksheet.write(row, 1, str(item["value"]))
                                except Exception:
                                    pass
                                row += 1
                        else:
                            for list_key in item.keys():
                                worksheet.write(row, 0, f"{key} - {list_key}")
                                worksheet.write(row, 1, item[list_key])
                                row += 1
                else:
                    worksheet.write(row, 0, key)
                    worksheet.write(row, 1, str(field))
                    row += 1
            workbook.close()
            output.seek(0)
            resp = HttpResponse(
                output.read(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            resp["Content-Disposition"] = f'attachment; filename="{filename}.xlsx"'
            return resp
        else:
            # CSV export
            import csv

            csv_response = HttpResponse(content_type="text/csv")
            csv_response["Content-Disposition"] = (
                f'attachment; filename="{filename}.csv"'
            )
            writer = csv.writer(csv_response)

            def get_sorted_keys(keys):
                ordered = []
                for key in [
                    "name",
                    "image",
                    "subtitle",
                    "data",
                    "relationships",
                    "map",
                    "link",
                    "enteredbyname",
                    "enteredbydate",
                    "modifiedbyname",
                    "modifiedbydate",
                ]:
                    if key in keys:
                        keys.remove(key)
                        ordered.append(key)
                return ordered + keys

            for key in get_sorted_keys(list(record_dict.keys())):
                field = record_dict[key]
                if (
                    isinstance(field, list)
                    and len(field) > 0
                    and isinstance(field[0], dict)
                ):
                    for item in field:
                        if "key" in item and "value" in item and len(item.keys()) == 2:
                            if (
                                isinstance(item["value"], list)
                                and len(item["value"]) > 0
                            ):
                                for sub_item in item["value"]:
                                    if (
                                        isinstance(sub_item, dict)
                                        and "name" in sub_item
                                    ):
                                        writer.writerow(
                                            [f"{key} - {item['key']}", sub_item["name"]]
                                        )
                                    else:
                                        writer.writerow(
                                            [f"{key} - {item['key']}", str(sub_item)]
                                        )
                            else:
                                writer.writerow(
                                    [f"{key} - {item['key']}", item["value"]]
                                )
                        else:
                            for list_key in item.keys():
                                writer.writerow([f"{key} - {list_key}", item[list_key]])
                else:
                    writer.writerow([key, str(field)])
            return csv_response


class DownloadMediaFile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, model_type, id):
        models = _get_model_by_type(model_type)
        if len(models) != 1:
            raise Http404
        model = models[0]
        try:
            obj = model.objects.get(pk=id)
        except Exception:
            raise Http404
        media = obj.media()
        import os
        from TEKDB.settings import MEDIA_ROOT

        file_path = os.path.join(MEDIA_ROOT, media["file"])
        if os.path.exists(file_path):
            with open(file_path, "rb") as fh:
                response = HttpResponse(
                    fh.read(), content_type="application/force-download"
                )
                response["Content-Disposition"] = (
                    f"attachment; filename={os.path.basename(file_path)}"
                )
                return response
        raise Http404


# ----- Export endpoints -----
class Download(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_category_list(self, request):
        categories = []
        for category in ["places", "resources", "activities", "sources", "media"]:
            if request.GET.get(category) == "true":
                categories.append(category)
        return categories

    def find_match_attributes(self, obj):
        match_attributes = [attr for attr in dir(obj) if "match" in attr]
        return match_attributes

    def get_greatest_similarity_attribute(self, result, pks):
        greatest_similarity_attribute = None
        matching_attributes = []

        # get headline and similarity results
        for match_attr in self.find_match_attributes(result):
            match_value = getattr(result, match_attr)
            if match_value is not None:
                if match_value == result.similarity:
                    matching_attributes.append(match_attr)

        # If multiple attributes have the same similarity, choose based on number of matching IDs
        if len(matching_attributes) == 1:
            greatest_similarity_attribute = matching_attributes[0]
        elif len(matching_attributes) > 0:
            num_same_id = pks[result.pk]
            if num_same_id - 1 < len(matching_attributes):
                greatest_similarity_attribute = matching_attributes[num_same_id - 1]
                pks[result.pk] -= 1
            else:
                greatest_similarity_attribute = matching_attributes[0]
        else:
            greatest_similarity_attribute = None

        return greatest_similarity_attribute

    def remove_match_prefix(self, string):
        if string.startswith("match_"):
            return string[6:]
        return string

    def get_verbose_field_name(self, model, field_path):
        parts = field_path.split("__")
        field = None
        current_model = model

        for part in parts:
            field = current_model._meta.get_field(part)

            # If it's a related field, follow to the related model
            if hasattr(field, "related_model") and field.related_model:
                current_model = field.related_model

        return (
            field.verbose_name.title()
            if field
            else field_path.replace("_", " ").title()
        )

    def get_results(self, keyword_string, categories):
        if keyword_string is None:
            keyword_string = ""

        resultlist = []

        for category in categories:
            query_models = _get_model_by_type(category)
            for model in query_models:
                # Find all results matching keyword in this model
                model_results = model.keyword_search(keyword_string)
                pks = {}
                # Count number of times each pk appears in results
                for result in model_results:
                    if hasattr(result, "pk"):
                        if result.pk not in pks:
                            pks[result.pk] = 1
                        else:
                            pks[result.pk] += 1

                for result in model_results:
                    actual_attribute = None
                    headline_value = None

                    greatest_similarity_attribute = (
                        self.get_greatest_similarity_attribute(result, pks)
                    )

                    actual_attribute = (
                        self.remove_match_prefix(greatest_similarity_attribute)
                        if greatest_similarity_attribute
                        else None
                    )
                    verbose_name = (
                        self.get_verbose_field_name(model, actual_attribute)
                        if actual_attribute
                        else None
                    )

                    headline_key = f"headline_{actual_attribute}"
                    if hasattr(result, headline_key):
                        headline_value = getattr(result, headline_key)

                    # Create JSON object to be returned
                    result_json = result.get_response_format()
                    if keyword_string != "":
                        result_json["rank"] = result.rank
                        result_json["similarity"] = result.similarity
                        result_json["headline"] = (
                            f"<p class='headline'>{verbose_name}: {headline_value}</p>"
                            if headline_value and verbose_name
                            else None
                        )
                    else:
                        result_json["rank"] = 0
                        result_json["similarity"] = 0
                        result_json["headline"] = None

                    resultlist.append(result_json)
        # Sort results from all models by rank, then similarity (descending)
        return sorted(
            resultlist, key=lambda res: (res["rank"], res["similarity"]), reverse=True
        )

    def get(self, request):
        categories = self.get_category_list(request)
        results = self.get_results(request.GET.get("query"), categories)
        format_type = request.GET.get("format")
        filename = "TEK_RESULTS"
        fieldnames = ["id", "name", "description", "type"]
        rows = []
        for row in results:
            row_dict = {}
            for field in fieldnames:
                row_dict[field] = row[field] if row[field] else " "
            rows.append(row_dict)

        if format_type == "xlsx":
            import io
            from xlsxwriter.workbook import Workbook

            output = io.BytesIO()
            workbook = Workbook(output, {"in_membory": True})
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({"bold": True})
            rows.insert(0, fieldnames)
            row = 0
            col = 0
            for entry in rows:
                for field in fieldnames:
                    if row == 0:
                        worksheet.write(0, col, field, bold)
                    else:
                        worksheet.write(row, col, entry[field])
                    col += 1
                row += 1
                col = 0
            workbook.close()
            output.seek(0)
            xls_response = HttpResponse(
                output.read(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            xls_response["Content-Disposition"] = (
                "attachment; filename=%s.xlsx" % filename
            )
            return xls_response

        else:
            # if format_type == 'csv':
            import csv

            csv_response = HttpResponse(content_type="text/csv")
            csv_response["Content-Disposition"] = (
                'attachment; filename="%s.csv"' % filename
            )
            writer = csv.DictWriter(csv_response, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
            return csv_response
