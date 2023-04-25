import json
from vk_api import VK_API
from YA_disk import YaUploader
from tqdm import tqdm


VK_TOKEN = ""
YA_TOKEN = ""

my_api = VK_API(VK_TOKEN)
my_ya_disk = YaUploader(YA_TOKEN)
id_user = "13141154"


def upload_photo(id_user, photo_count=5):
    data = my_api.photos_get(id_user)
    # Выбираем 5 самых больших фото
    best_photo = sorted(data, key=lambda x: x["size"], reverse=True)[0:photo_count]
    name_folder = "MyFolder"
    my_ya_disk.create_folder(name_folder)

    for item in tqdm(best_photo, desc='Сохранение фотографий на Яндекс диске'):
        my_ya_disk.upload_file(name_folder, item)

    # Записываем данные о всех скаченных фотографиях в файл .json
    with open("photos.json", "w") as file:
        json.dump(best_photo, file, indent=2)


if __name__ == "__main__":
    upload_photo(id_user)
