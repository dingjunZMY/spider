import re 
from urllib import request
class Reptile():
    #url='https://book.douban.com/top250'
    #urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,226,25)]
    root_pattern='<div class="pl2">([\s\S]*?)</div>'
    urls_pattern='<a href="([\s\S]*?)"'
    bookname_pattern='<span property="v:itemreviewed">([\s\S]*?)</span>'
    bookinfos_pattern='<div id="info" class="">([\s\S]*?)</div>'

    def __fetch_content(self,url):
        r=request.urlopen(url)
        htmls=r.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        htmls=re.findall(Reptile.root_pattern,htmls)
        urls=[]
        for html in htmls:
            url=re.findall(Reptile.urls_pattern,html)
            urls.append(''.join(url))
        return urls

    def __fetch_content1(self,urls):
        """ 
        根据url向详细页发送请求
        """
        anchors=[]
        books=[]
        for url in urls:
            r=request.urlopen(url)
            htmls=r.read()
            htmls=str(htmls,encoding='utf-8')
            anchors.append(htmls)
        for anchor in anchors:
            book_name=re.findall(Reptile.bookname_pattern,anchor)
            bookinfos=re.findall(Reptile.bookinfos_pattern,anchor)#获取一本书的全部信息
            bookinfo=re.sub(r'<[^>]+>','',bookinfos[0])
            book_content={'name':book_name,'info':bookinfo}
            books.append(book_content)
        return books
    #抓取数据，数据精炼
    def __refine(self,books):
        l=lambda book: {
            'name':book['name'][0],
            'info':book['info'].replace('\n','').replace('&nbsp;','').strip()
            }
        return map(l,books)

    def __show(self,books):
        for i in range(0,len(books)):
            print('书名字：'+books[i]['name']+'\n'+'======================='+'\n'
            +'书的基本信息：'+books[i]['info']+'\n'+'======================================================='+'\n')

    def go(self,url):
        htmls=self.__fetch_content(url)
        urls=self.__analysis(htmls)
        books=self.__fetch_content1(urls)
        books=list(self.__refine(books))
        self.__show(books)
        
reptile=Reptile()



