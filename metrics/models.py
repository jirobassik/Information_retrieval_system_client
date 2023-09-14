class MetricModel:
    def __init__(self, recall, precision, accuracy, error, fmeasure, middle_metric, precision_n, list_recall,
                 list_precision):
        self.recall = recall
        self.precision = precision
        self.accuracy = accuracy
        self.error = error
        self.fmeasure = fmeasure
        self.middle_metric = middle_metric
        self.precision_n = precision_n
        self.list_recall = list_recall
        self.list_precision = list_precision
