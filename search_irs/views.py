import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import cgi
from utils.init_json_ser_req import query_request, query_json_serializer, download_request, \
    classification_request, classification_json_serializer
from utils.queryset_upl import file_queryset_upl


def search(request):
    if 'query_button' in request.POST:
        return handle_query_request(request)
    return show_main_view(request)


def handle_query_request(request):
    user_query = request.POST['query']
    serialize_query = query_json_serializer.encode(query=user_query)
    data_query_request = query_request.get_request_data(serialize_query)
    dict_filenames = json.loads(data_query_request)
    queryset_file = file_queryset_upl()
    return render(request, 'search_irs/search.html',
                  {'dict_filenames': dict_filenames, 'files': queryset_file, 'query': user_query,
                   'empty_dict': next(iter(dict_filenames.values())) })


def show_main_view(request):
    queryset_file = file_queryset_upl()
    return render(request, 'search_irs/main_view.html', {'files': queryset_file})


def classification_text_file(request, pk):
    classification_content_request = classification_request.detail_get_request(id=pk)
    if classification_content_request.status_code == 200:
        queryset_classification = classification_json_serializer.decode(classification_content_request.content,
                                                                        many=False)
        return render(request, 'search_irs/classific.html', {'class': queryset_classification})
    return HttpResponseRedirect(reverse('search'))


def download_file(request, pk):
    file_data, content_disposition = download_request.detail_get_request_file(id=pk)
    _, params = cgi.parse_header(content_disposition)
    filename = params.get('filename')
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
