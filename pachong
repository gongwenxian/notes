
# 网络爬虫
### python 2.x里面urllib2和python 3.x里面的urllib 有些不同
里面的一些模块被分成urllib.request urllib.parse 和urllib.error。

### BeatifulSoup解析器 区分在python单独的库
常用的是beautifulsoup对象 
eg: from bs4 import BeautifulSoup
BeautifulSoup(content,"type")
#### type
有四种：
html.parse:(这种解析方式在Python2.7.3之前，中文兼容性比较差)
lxml:主要是lxml.html(需要安装C语言库)
xml:主要是lxml.xml(需要安装C语言库)
html5lib:速度比较慢，不支持外部扩展


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.baidu.com")
bsobj=BeautifulSoup(html.read(),"lxml")
#bsobj结构可以看成（html-body-h1）,调用取值的话，可以直接用bsobj.h1或者bsobj.html.body.h1
type(bsobj)
```




    bs4.BeautifulSoup




```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj=BeautifulSoup(html.read(),"lxml")
        title=bsobj.body.h1
    except AttributeError as e:
        return None
    return title

title=getTitle("http://www.baidu.com")
if title ==None:
    print("Title couldn't be found!")
else:
    print(title)
```

    Title couldn't be found!


## 获取指定标签

bsobj.findall(tagName,tagAttributes) 获取指定的所有标签，后面的是字典。
.get_text() 会吧超链接、符号、源代码等全部去掉，只剩下一串不带标签的含文字的字符串。

### find(tag,attributes,recursive,text,limit,keywords) 和findAll(ag,attributes,recursive,text,limit,keywords)
一般只会用到前两个参数。
第三个参数：recursive为Boolean值，表示是否查询子标签和子标签的子标签。
findAll()的recursive属性默认为true。
bsobj.findAll(text="aaa")
bsobj.findAll(id="text")==> bsobj.findAll("",{"id":"text"})
bsobj.findAll(class="green")里面的class有歧义，用一个交标区分：class_="green"

## 正则表达式
### 常用符号
    * 出现0次或者多次
    + 出现1次或者多次
    [] 匹配任意一个
    () 表达式编组
    {m,n} 匹配前面的子式m次或者n次
    [^] 不取里面任何一个
    | 任意匹配一个
    . 匹配任意一个字符（包括括号啥的）
    \ 转义符号
    ^ $ 开始结束
    ?! 不包含


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.baidu.com")
bsobj=BeautifulSoup(html.read(),"lxml")
for link in bsobj.findAll("a"):
   if "href" in link.attrs:
        print(link.attrs["href"])
```

    /
    javascript:;
    javascript:;
    javascript:;
    /
    javascript:;
    https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5
    http://news.baidu.com
    http://www.hao123.com
    http://map.baidu.com
    http://v.baidu.com
    http://tieba.baidu.com
    http://xueshu.baidu.com
    https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5
    http://www.baidu.com/gaoji/preferences.html
    http://www.baidu.com/more/
    http://news.baidu.com/ns?cl=2&rn=20&tn=news&word=
    http://tieba.baidu.com/f?kw=&fr=wwwt
    http://zhidao.baidu.com/q?ct=17&pn=0&tn=ikaslist&rn=10&word=&fr=wwwt
    http://music.baidu.com/search?fr=ps&ie=utf-8&key=
    http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=
    http://v.baidu.com/v?ct=301989888&rn=20&pn=0&db=0&s=25&ie=utf-8&word=
    http://map.baidu.com/m?word=&fr=ps01000
    http://wenku.baidu.com/search?word=&lm=0&od=0&ie=utf-8
    //www.baidu.com/more/
    //www.baidu.com/cache/sethelp/help.html
    http://home.baidu.com
    http://ir.baidu.com
    http://e.baidu.com/?refer=888
    http://www.baidu.com/duty/
    http://jianyi.baidu.com/
    http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000001


## 调用API

token="<your api key>"
webRequest=urllib.request.Request("url",headers={"token"})
html=urlopen(webRequest)

# 存储数据

## urllib.request.urlretrieve 下载文件，根据url
(url,path,name)三个参数


```python
import pymysql
#数据库连接
conn=pymysql.connect(host='localhost',unix_socket='/tmp/mysql.sock',user='root',password='113036',db='mysql',charset='utf8')
conn
#光标
cur=conn.cursor()
#传达sql指令
cur.execute("use mysql")
cur.execute("select * from user")
#显示结果
print(cur.fetchone())
#一定要记得关掉
cur.close()
conn.close()
```

    ('localhost', 'root', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '', b'', b'', b'', 0, 0, 0, 0, 'mysql_native_password', '*5DE4B7A0FC0682825EBFDD68883D75B4F2344FF8', 'N', datetime.datetime(2017, 8, 21, 18, 17, 18), None, 'N')



```python
import smtplib
from email.mime.text import MIMEText
msg=MIMEText("hello body")
msg['Subject']="AN Email alert"
msg['From']='liuyifei'
msg['To']='gongwenxian123@163.com'

#s=smtplib.SMTP('localhost')
#s.send_message(msg)
#s.quit()
```

## 发送邮件，有待商榷

# 图像识别和文字处理

## ocr库概述
* pillow
* tesseract

