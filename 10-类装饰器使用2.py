from re import T


class Test(object):
    
    def __init__(self,func):
        print("---init---方法")
        print("---func---",func)
        #func 是login函数的引用
        self.func = func
    
        
    def __call__(self, *args, **kwargs):
        print("---开始验证---")
        #调用原来login的内容
        self.func()
        
@Test   #这边装饰完后到__init__(self,func):这个函数
# login = Test(login)
def login():
    print("开始登陆")
    
login()