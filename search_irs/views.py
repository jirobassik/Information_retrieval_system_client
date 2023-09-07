import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import cgi
import speech_recognition as sr
from utils.init_json_ser_req import file_request, query_request, query_json_serializer, download_request
from utils.queryset_upl import file_queryset_upl


def search(request):
    if 'query_button' in request.POST:
        return handle_query_request(request)
    elif 'upl' in request.POST:
        handle_upl_request(request)
    return show_main_view(request)


def handle_upl_request(request):
    if upl_file := request.FILES.get('document', False):
        file_request.post_request_file(upl_file)


def handle_query_request(request):
    serialize_query = query_json_serializer.encode(query=request.POST['query'])
    data_query_request = query_request.get_request_data(serialize_query)
    dict_filenames = json.loads(data_query_request)
    queryset_file = file_queryset_upl()
    return render(request, 'search_irs/search.html', {'dict_filenames': dict_filenames, 'files': queryset_file})


def show_main_view(request):
    queryset_file = file_queryset_upl()
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


def speech_to_text(request):
    recognizer = sr.Recognizer()
    print('start micro')
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.listen(source)
            text = recognizer.recognize_google(audio_data)

        except sr.UnknownValueError:
            text = "Could not understand the audio"
        except sr.RequestError as e:
            text = f"Speech recognition error: {str(e)}"
    print('django text', text)
