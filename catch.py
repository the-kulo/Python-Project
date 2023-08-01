#抓取网页的原始码（HTML）
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一个Request物件，附加Request Headers的资讯
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#解析原始码
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
#寻找class="titles"的所有div标签
title=root.find_all("div",class_="title")
print(title)
