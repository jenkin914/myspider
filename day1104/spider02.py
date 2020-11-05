from urllib.request import Request, urlopen
from urllib.parse import quote


def zhihu():
    url = 'https://zhuanlan.zhihu.com/p/26122321'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3'
                      '6 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    request = Request(url=url, headers=headers)
    response = urlopen(request)
    assert response.code == 200
    bytes_ = response.read()
    print(bytes_)
    with open('zhihu.html', 'wb') as file:
        file.write(bytes_)


if __name__ == '__main__':
    zhihu()
