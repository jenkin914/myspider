"""
初次使用urllib实现数据请求
urllib.request.urlopen(url) 发起get请求
urllib.parse.quote() 将中文进行url编码
urllib.request.urlretrieve(url, filename) 下载url保存到filename
"""
from urllib.request import urlopen, urlretrieve, Request
from urllib.parse import quote


def search_baidu(wd=None):
    # 网络资源接口（url）
    base_url = 'http://www.baidu.com/s?wd=%s'
    url = base_url % quote(wd)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3'
                      '6 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    request = Request(url=url, headers=headers)
    response = urlopen(request)
    # 添加断言 相当于if语句
    assert response.code == 200
    print('请求成功')
    bytes_ = response.read()
    with open('%s.html' % wd, 'wb') as file:
        file.write(bytes_)


if __name__ == '__main__':
    search_baidu(wd=input("请输入检索内容："))
