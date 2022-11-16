import requests
from Ya_token import TOKEN
from pprint import pprint

print('Task 1\n')

all_superheroes = {'Hulk':332, 'Captain_America':149, 'Thanos':655}
new_superheroes = {}
for v in all_superheroes.values():
    url = 'https://akabab.github.io/superhero-api/api' + f'/id/{v}.json'
    req = requests.get(url).json()
    new_superheroes[req['name']]=req['powerstats']['intelligence']
print('Самый умный супергерой: ', max(new_superheroes))

print('\n', '#'*20, '\n')

print('Task 2\n')

class YaUploader():
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    def __init__(self, token, file_path):
        self.token = token
        self.file_path = file_path
        self.params = {
            'path' : self.file_path, 
            'overwrite': 'true'
            }
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
            } 

    def upload(self):
        link = f'{YaUploader.url}/upload'
        req = requests.get(url=link, headers=self.headers, params=self.params)
        href = req.json().get('href')
        req = requests.put(href, data=open('test.txt', 'rb'))
        req.raise_for_status()
        if req.status_code == 201:
            print("Success")
        
def main():
    Upload = YaUploader(token=TOKEN, file_path=r'\Projects\test.txt')
    Upload.upload()

if __name__ == '__main__':
    main()

print('\n', '#'*20, '\n')

print('Task 3\n')

url = 'https://api.stackexchange.com/2.3/questions'

params = {
    'fromdate' : 1668384000,
    'todate' : 1668556800,
    'order' : 'desc',
    'sort' : 'activity',
    'tagged' : 'python',
    'site' : 'stackoverflow'
}

req = requests.get(url=url, params=params).json()
pprint(req)