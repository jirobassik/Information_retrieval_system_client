from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import cgi
from utils.init_json_ser_req import file_request, download_request
from utils.queryset_upl import file_queryset_upl


def view_file(request):
    if 'upl' in request.POST:
        handle_upl_request(request)
    return show_main_view(request)


def handle_upl_request(request):
    if upl_file := request.FILES.get('document', False):
        file_request.post_request_file(upl_file)


def show_main_view(request):
    queryset_file = file_queryset_upl()
    return render(request, 'view_files/view_file.html', {'files': queryset_file})


def delete_file(request, pk):
    file_request.delete_request(id=pk)
    return HttpResponseRedirect(reverse('view_file'))


def download_file(request, pk):
    file_data, content_disposition = download_request.detail_get_request_file(id=pk)
    _, params = cgi.parse_header(content_disposition)
    filename = params.get('filename')
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
