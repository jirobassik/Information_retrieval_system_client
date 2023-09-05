from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=1000)


class FileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    upload_file = serializers.CharField()
