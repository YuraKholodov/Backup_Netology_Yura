import requests


class YaUploader:
    def __init__(self, token: str):
        self.__token = token

    def get_headers(self):
        return {
            "Content_Type": "application/json",
            "Authorization": f"OAuth {self.__token}",
        }

    def create_folder(self, name: str):
        url_create_folder = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": name, "overwrite": "false"}
        requests.put(url=url_create_folder, headers=headers, params=params)

    def upload_file(self, name_folder, item):
        download_file = requests.get(url=item["url"]).content
        url_create_folder = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        name_file = item["file_name"]
        params = {"path": f"{name_folder}/{name_file}"}
        response = requests.get(url=url_create_folder, headers=headers, params=params)
        try:
            href = response.json()["href"]
            requests.put(href, download_file)
        except KeyError:
            print("Файл уже был сохранен ранее!!!")
