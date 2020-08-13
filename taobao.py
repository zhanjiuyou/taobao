#2020年8月10日
#该爬虫主要完成爱淘宝网站的登录商品销量和排行等爬取
#由于淘宝网站是异步加载的，只能使用selenium调用浏览器爬取
#我的个人博客: https://jiaokangyang.com

#添加注释

import requests
from selenium import webdriver

s = webdriver.Chrome()