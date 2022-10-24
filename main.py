import requests
from datetime import datetime, timedelta

# heroes = ['Steppenwolf', 'Sylar', 'Gamora']
heroes = ['Hulk', 'Captain America', 'Thanos']
heroes_stats = {}
def superheroes(heroes):
    url ='https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    if response.status_code == 200:
        heroes_list = response.json()
        for i in heroes_list:
            if i['name'] in heroes:
                heroes_stats[f"{i['name']}"] = i['powerstats']['intelligence']
    max_val = max(heroes_stats.items(), key=lambda x: x[1])
    print(f'Самый умный из них: {max_val[0]} - {max_val[1]}.')

######################### YandexDisk ##################################
TOKEN = ''
class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true' }
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()
    def upload(self, file_path: str, file_name):
        result = self._get_upload_link(file_path=file_path)
        href = result.get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Created')

######################### Stackoverflow ##################################
last_data = int((datetime.now()-timedelta(hours=48)).timestamp())
def get_questions(fromdate, tag):
    url = f'https://api.stackexchange.com/2.3/questions?fromdate={fromdate}&order=desc&sort=activity&tagged={tag}&site=stackoverflow'
    response = requests.get(url)
    if response.status_code == 200:
        question_list = response.json()
        print(f'Вопросы на stackoverflow за последние 2 дня, c тегом "{tag}":')
        count = 0
        for i in question_list['items']:
            count += 1
            print(f'{count}. {i["title"]}')

if __name__ == '__main__':
    superheroes(heroes)
    ya = YaUploader(token=TOKEN)
    ya.upload('test_upload_yadisk.txt', 'for_yadisk.txt')
    get_questions(last_data, 'Python')