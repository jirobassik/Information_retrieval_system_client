from search_irs.serializers import FileSerializer, SearchSerializer
from search_irs.models import FileModel, QueryModel

from utils.request_server import Request
from utils.json_serializer import JsonSerializer

file_json_serializer = JsonSerializer(FileModel, FileSerializer)
file_request = Request.uploadfiles_model()

query_json_serializer = JsonSerializer(QueryModel, SearchSerializer)
query_request = Request.search_model()

download_request = Request.download_model()
