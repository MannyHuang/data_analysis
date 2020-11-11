import requests
import json


def picDownload(src, id):
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        picFile = open(dir, 'wb')
        picFile.write(pic.content)
        picFile.close()
    except requests.exceptions.ConnectionError:
        print('error')


query = '王祖贤'

for i in range(0, 22471, 20):
    url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start='+str(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36'}
    html = requests.get(url,headers=headers).text
    response = json.loads(html, encoding='utf-8')
    for image in response['images']:
        picDownload(image['src'], image['id'])

