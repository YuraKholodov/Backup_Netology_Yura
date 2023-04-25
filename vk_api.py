import requests


class VK_API:
    URL = "https://api.vk.com/method/"

    def __init__(self, token: str) -> None:
        self.__params = {"access_token": token, "v": "5.131"}

    def photos_get(self, owner_id):
        """Получаем список словарей всех фотографий в максимальном размере"""

        photo_library = []
        name_photo = []
        url_get = self.URL + "photos.get"
        params = {"owner_id": owner_id, "album_id": "profile", "extended": 1}
        params_get = {**self.__params, **params}
        res = requests.get(url=url_get, params=params_get).json()

        for photo in res["response"]["items"]:

            if "?" in photo["sizes"][-1]["url"]:
                file_type = photo["sizes"][-1]["url"].split("?")[0].split(".")[-1]
            else:
                file_type = photo["sizes"][-1]["url"].split(".")[-1]

            data = {
                "file_name": str(photo["likes"]["count"]) + "." + file_type,
                "size": photo["sizes"][-1]["type"],
                "url": photo["sizes"][-1]["url"],
                "date": photo["date"],
            }
            #Проверяем имена фото на дубли. Если дубль есть, дописываем дату создания
            name_photo.append(data["file_name"])
            if name_photo.count(data["file_name"]) != 1:
                data["file_name"] = str(photo['date']) + '_' + data["file_name"]
            photo_library.append(data)

        return photo_library
