import os
import docx
import re
class docx_find(object):
    def __init__(self,directory,find_content):
        self.directory=directory
        self.find_content=find_content

        self.lz_find()
        self.doc_content()

    def lz_find(self):
        lz=[]
        t=os.walk(self.directory)
        for i in t:
            for j in i[2]:
                p=os.path.splitext(j)
                if p[1] == '.docx':
                    lz.append(os.path.join(i[0],j))
        print('目录下找到docx文件:%d'%len(lz))
        self.lz=lz

    def content_find(self,content):
        data=re.findall(self.find_content,content)
        if(len(data)==0):
            return 0
        else:
            return len(data)

    def doc_content(self):
        result={}
        content=''
        for i in self.lz:
            try:
                doc=docx.Document(i)
                for j in doc.paragraphs:
                    content=content+j.text
                p=self.content_find(content)
                if(p!=0):
                    result[i]=p
            except:
                pass
        if (len(result) !=0):
            for i in result.keys():
                print('在\t%s\t,出现 %d 次'%(i,result[i]))
            print('共%d个结果'%len(result))
        else:
            print('搜索没有结果')


ml=input('输入目录:')
find_content=input('查找内容:')
one=docx_find(ml,find_content)
