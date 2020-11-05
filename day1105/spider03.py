from urllib.request import Request, urlopen, urlretrieve
from urllib.parse import quote


def download_img():
    # 从url中拿文件名
    url = 'https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/03/06/ChMlWl8VC' \
          'gmICd2wACqdJHniwRMAAQCnwOff8UAKp08416.jpg'
    filename = url[url.rfind('/') + 1:]
    print(filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3'
                      '6 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    with open(filename, 'wb') as file:
        file.write(response.read())
    print(f'下载{filename}  OK!')


if __name__ == '__main__':
    download_img()
