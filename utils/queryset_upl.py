from utils.init_json_ser_req import file_request, file_json_serializer


def file_queryset_upl():
    raw_data_file = file_request.get_request()
    return file_json_serializer.decode(raw_data_file)
