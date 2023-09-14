from rest_framework import serializers


class MetricSerializer(serializers.Serializer):
    recall = serializers.FloatField()
    precision = serializers.FloatField()
    accuracy = serializers.FloatField()
    error = serializers.FloatField()
    fmeasure = serializers.FloatField()
    middle_metric = serializers.FloatField()
    precision_n = serializers.FloatField()
    list_recall = serializers.ListField()
    list_precision = serializers.ListField()
