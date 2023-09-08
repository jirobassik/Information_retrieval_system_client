from search_irs.serializers import FileSerializer, SearchSerializer, ClassificationSerializer
from search_irs.models import FileModel, QueryModel, ClassificationModel

from utils.request_server import Request
from utils.json_serializer import JsonSerializer

file_json_serializer = JsonSerializer(FileModel, FileSerializer)
file_request = Request.uploadfiles_model()

query_json_serializer = JsonSerializer(QueryModel, SearchSerializer)
query_request = Request.search_model()

classification_json_serializer = JsonSerializer(ClassificationModel, ClassificationSerializer)
classification_request = Request.classification_model()

download_request = Request.download_model()

