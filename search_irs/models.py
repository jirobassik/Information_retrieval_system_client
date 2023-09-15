class FileModel:
    def __init__(self, id, upload_file, file_content):
        self.id = id
        self.upload_file = upload_file
        self.file_content = file_content


class QueryModel:
    def __init__(self, query):
        self.query = query


class ClassificationModel:
    def __init__(self, text_class, filename):
        self.text_class = text_class
        self.filename = filename
