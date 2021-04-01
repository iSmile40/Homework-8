import requests
from pprint import pprint

# Задание 1

super_heroes_list = ["Hulk", "Captain America", "Thanos"]

def compare_intelligence(super_heroes_list):
    max_intelligence = 0
    max_intelligence_hero = 0
    super_heroes_dict = dict.fromkeys(super_heroes_list)

    for hero in super_heroes_list:
        url = "https://superheroapi.com/api/2619421814940190/search/" + hero
        responce = requests.get(url, timeout=5).json()
        # pprint(responce)
        super_heroes_dict[hero] = int(responce['results'][0]['powerstats']['intelligence'])
        # print(super_heroes_dict[hero])

    for hero in super_heroes_dict:
        if max_intelligence < super_heroes_dict[hero]:
            max_intelligence = super_heroes_dict[hero]
            max_intelligence_hero = hero

    return f'Самый умный супергерой с интеллектом {max_intelligence} - {max_intelligence_hero}'

# print(compare_intelligence(super_heroes_list))

# Задание 2

Token = "Your token"

class YandexDisk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        responce = requests.get(upload_url, headers=headers, params=params)
        return responce.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        responce = requests.put(href, data=open(filename, "rb"))
        responce.raise_for_status()
        if responce.status_code == 201:
            return "Success"

if __name__ == '__main__':
    yandex_disk = YandexDisk(token=Token)
    print(yandex_disk.upload_file_to_disk("Homework-8/homework.txt", "file.txt"))
