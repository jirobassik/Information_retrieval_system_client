import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import cgi

from utils.init_json_ser_req import file_request, file_json_serializer, query_request, query_json_serializer, \
    download_request


def search(request):
    if 'query_button' in request.POST:
        serialize_query = query_json_serializer.encode(query=request.POST['query'])
        data_query_request = query_request.get_request_data(serialize_query)
        dict_filenames = json.loads(data_query_request)
        return render(request, 'search_irs/search.html', {'dict_filenames': dict_filenames})
    if 'upl' in request.POST:
        if upl_file := request.FILES.get('document', False):
            file_request.post_request_file(upl_file)
    raw_data_file = file_request.get_request()
    queryset_file = file_json_serializer.decode(raw_data_file)
    return render(request, 'search_irs/main_view.html', {'files': queryset_file})


def delete_file(request, pk):
    file_request.delete_request(id=pk)
    return HttpResponseRedirect(reverse('search'))


def download_file(request, pk):
    file_data, content_disposition = download_request.detail_get_request(id=pk)
    _, params = cgi.parse_header(content_disposition)
    filename = params.get('filename')
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
