import requests
import re
from lxml import etree
import collections


# 获取网页的所有单词
def execute(url):
    print(url)
    response = requests.get(url)
    # 获取单词的正则表达式
    pattern1 = re.compile('[a-zA-Z]+')
    # 去除 html 标签的正则表达式
    pattern2 = re.compile('<script.*?script>|<style.*?style>|<!--.*?-->|<[^>]+>', re.S)
    response = re.sub(pattern2, '', response.text)
    result = re.findall(pattern1, response)
    print(result)
    return result


# 获取该网页所有的内部链接
def get_all_url():
    # domain 与 url 需要手动填入
    # domain = 'https://kubernetes.io/'
    # url = 'https://kubernetes.io/docs/home/'
    # domain = 'https://docs.docker.com/'
    # url = 'https://docs.docker.com/'
    response = requests.get(url)
    html = etree.HTML(response.text)
    href = html.xpath('//a/@href')
    result = []
    for item in href:
        if '#' not in item and 'http' not in item and 'javascript' not in item:
            result.append(domain + item)
    return set(result)


# 统计整个网站的词频
def statistics(result):
    result = [x.lower() for x in result]
    result = collections.Counter(result)
    with open('./translate', 'a', encoding='utf8') as f:
        for k,v in result.items():
            f.write(k + ' ' + str(v) + '\n')


if __name__ == '__main__':
    urls = get_all_url()
    result = []
    for url in urls:
        temp_result = execute(url)
        result += temp_result
    statistics(result)
