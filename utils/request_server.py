import requests


class Request:
    def __init__(self, model_name: str):
        self.__model_name = model_name

    @classmethod
    def search_model(cls):
        return cls('search')

    @classmethod
    def uploadfiles_model(cls):
        return cls('uploadfiles')

    @classmethod
    def download_model(cls):
        return cls('download')

    def get_request(self):
        return requests.get(f'http://127.0.0.1:8001/api/v1/{self.model_name}/').content

    def get_request_data(self, data: str):
        return requests.get(f'http://127.0.0.1:8001/api/v1/{self.model_name}/', data=data,
                            headers={'Content-Type': 'application/json'}).content

    # def detail_get_request(self, id):
    #     return requests.get(f'http://127.0.0.1:8001/api/v1/{self.model_name}/{id}')
    def detail_get_request(self, id):
        response = requests.get(f'http://127.0.0.1:8001/api/v1/{self.model_name}/{id}')
        return response.content, response.headers.get('Content-Disposition')

    def post_request(self, data: dict):
        requests.post(f'http://127.0.0.1:8001/api/v1/{self.model_name}/', data=data,
                      headers={'Content-Type': 'application/json'})

    def post_request_file(self, file):
        requests.post(f'http://127.0.0.1:8001/api/v1/{self.model_name}/', files={'upload_file': file})

    def put_request(self, data, id):
        requests.put(f'http://127.0.0.1:8001/api/v1/{self.model_name}/{id}/', data=data,
                     headers={'Content-Type': 'application/json'})

    def delete_request(self, id):
        requests.delete(f'http://127.0.0.1:8001/api/v1/{self.model_name}/{id}/')

    @property
    def model_name(self):
        return self.__model_name
