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
