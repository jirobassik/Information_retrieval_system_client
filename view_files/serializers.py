from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    upload_file = serializers.CharField()
