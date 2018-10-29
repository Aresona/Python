# Scrapy 框架
## 功能
* 应用 twisted, 下载页面
* HTML 解析对象
* 代理
* 延迟下载
* 自动去重
* 深度(找几层)与广度
## 原理猜想
0. Scrapy Engine
1. 起始 URL
2. 下载页面(持久化、继续下载)
3. 调度器(Scheduler)
4. 下载器(Downloader)
5. Spiders(回调函数)(需要操作)
6. Item Pipeline(持久化)(需要操作)

![](https://images2015.cnblogs.com/blog/425762/201605/425762-20160507220247421-1722096301.png)

## 安装
它在 python3 里面没有完全支持，主要是 twsted 的支持
### Linux or Mac
<pre>
pip3 install scrapy
</pre>
### Windows
<pre>
pip3 install scrapy
</pre>
> 在安装 scrapy 时会报 twsted 的错，装 twisted 也会报错

解决方法:
<pre>
下载 pywin32
pip3 install wheel
D:\\twisted...wheel
pip3 install D:\\twisted...wheel
pip3 install scrapy
</pre>

检测方法:
<pre>
python3
import scrapy
</pre>

> 在 python3 里，对 twisted 未完全支持，但未支持功能我们基本用不着,我们只需要它下载那一块

## 使用
<pre>
guohui:python guohui$ scrapy startproject sp1
New Scrapy project 'sp1', using template directory '/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/scrapy/templates/project', created in:
    /Users/guohui/python/sp1

You can start your first spider with:
    cd sp1
    scrapy genspider example example.com
guohui:python guohui$ cd sp1/
guohui:sp1 guohui$ tree
.
├── scrapy.cfg    # 配置文件，主要指教向 settings.py
└── sp1
    ├── __init__.py
    ├── __pycache__
    ├── middlewares.py   中间件
    ├── items.py     格式化
    ├── pipelines.py    持久化
    ├── settings.py    配置文件
    └── spiders    爬虫
        ├── __init__.py
        └── __pycache__
guohui:sp1 guohui$ cd sp1
guohui:sp1 guohui$ scrapy genspider baidu baidu.com
Created spider 'baidu' using template 'basic' in module:
  sp1.spiders.baidu
guohui:sp1 guohui$ cd spiders/  # 创建爬虫，一个项目可以创建多个爬虫，爬取多个网站
guohui:spiders guohui$ cat baidu.py 
# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
# 进入项目(spiders)的上级目录，并执行爬虫
cd sp1
scrapy crawl baidu --nolog
</pre>

### settings.py

<pre>
# Obey(遵守) robots.txt rules (爬虫协议)
ROBOTSTXT_OBEY = False
</pre>

### 基本使用及选择器
