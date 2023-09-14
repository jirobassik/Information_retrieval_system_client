from django.shortcuts import render
from utils.init_json_ser_req import query_json_serializer, metrics_request, metric_json_serializer


def metrics(request):
    if 'metric_button' in request.POST:
        return metric_search_view(request)
    return metric_main_view(request)


def metric_main_view(request):
    return render(request, 'layout_metric.html')


def metric_search_view(request):
    serialize_query = query_json_serializer.encode(query=request.POST['query_metrics'])
    metric_request_content_raw = metrics_request.get_request_data(data=serialize_query)
    metric_request_content = metric_json_serializer.decode(metric_request_content_raw, many=False)
    return render(request, 'metrics/metric_calc.html', {'metrics': metric_request_content, })
