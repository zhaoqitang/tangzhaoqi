""" 
也有人讲这种方式成为   装饰器工厂模式

装饰器写法：
1.存在闭包
2.存在带修饰的函数
"""


def test(path):
    print(path)
    
    """ 外层函数 """
    def function_out(func):
        
        """ 内层函数 """
        def function_in():
            print("开始验证")
            func()
            
        """ 返回内层函数的引用 """
        return function_in
    """ 返回装饰器的引用 """
    return function_out

@test("login") # 底层 login = test(login)
#@test("login") 分解为两步
#1. test("login")  --》 function_out  引用
#2. @ 一步的结果     --》 @function_out

#下一步:
#login = function_out(function)  如果没有参数，直接进行这一步

def login():
    print("开始登录")
    
    
@test("resister")
def resister():
    print("开始注册")
    
login()
resister()