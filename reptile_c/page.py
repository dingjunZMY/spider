import re
from urllib import request
from reptile import Reptile
urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(175,226,25)]
print(urls)
for url in urls:
    Reptile().go(url)




