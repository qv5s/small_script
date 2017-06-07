import pickle
import os
import time
import  msvcrt
class UM(object):
    def __init__(self):
        self.file_o()
        self.choice()
        self.file_c()
    def file_o(self):
        file=os.path.dirname(__file__)
        self.file_o=file+'/账号管理.txt'
        self.file_n=file+'/账号管理.pkl'
        if os.path.exists(self.file_o):
            os.rename(self.file_o, self.file_n)
        elif os.path.exists(self.file_n):
            pass
        else:
            f=open(self.file_n,'wb')
            data={}
            pickle.dump(data,f)
            f.close()
            print('不存在目标文件，已创建')
        f = open(self.file_n, 'rb')
        self.data = pickle.load(f)
        f.close()
        os.rename(self.file_n, self.file_o)

    def file_c(self):
        os.rename(self.file_o, self.file_n)
        f=open(self.file_n,'wb')
        pickle.dump(self.data,f)
        f.close()
        os.rename(self.file_n, self.file_o)

    def choice(self):
        while (True):
            print('------------------')
            print('1.查看账号密码')
            print('2.修改账号密码')
            print('3.删除账号密码')
            print('4.增加应用信息')
            print('------------------')
            n = input('Please input number:')
            self.check_user(n)

    def check_user(self, n):
        while (True):
            if (n != '1' and n != '2' and n != '3' and n != '4'):
                print('输入错误')
                self.choice()
            if (n == '4'):
                print('应用名称:', end=' ')
                key = input()
                if (self.data.get(key) == None):
                    value = input('value:')
                    self.data[key] = value
                    self.file_c()
                    print('添加成功。按任意键退出')
                    ch = msvcrt.getch()
                    exit()
                else:
                    print('应用已存在')
                    self.choice()
            print('输入应用名称：', end=' ')
            name = input()
            content = self.data.get(name)
            if (content != None):
                print('------------------')
                print(name + ':', end=' ')
                print(content)
                print('------------------')
                if (n == '1'):
                    self.file_c()
                    print('按任意键退出')
                    ch = msvcrt.getch()
                    exit()
                elif (n == '2'):
                    print('输入修改信息:')
                    value = input('value:')
                    try:
                        self.data[name] = value
                        self.file_c()
                        print('修改成功')
                        print('按任意键退出')
                        ch = msvcrt.getch()
                        exit()
                    except:
                        print('修改失败')
                elif (n == '3'):
                    print('确认删除,yes/no:', end=' ')
                    q = input()
                    if (q == 'yes'):
                        del (self.data[name])
                        self.file_c()
                        print('按任意键退出')
                        ch = msvcrt.getch()
                        exit()
                    else:
                        self.choice()


            else:
                print('------------------')
                print('没有该应用信息')
                time.sleep(3)
                self.choice()
one=UM()

