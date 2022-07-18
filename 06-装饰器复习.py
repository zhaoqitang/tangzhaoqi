""" 
闭包结构：
1. 存在函数的嵌套关系
2. 内存可以使用外层的变量
3.外层返回内层的引用
"""

# def function_out(num):
    
#     def function_in():
        
#         print("num = ",num)
        
#     return function_in


# ret = function_out(10)
# ret()


def function_out(func):
    
    def function_in():
        
        print("开始验证")
        func() #这边是装饰器执行完以后，login赋值给了func，然后func()就调用了login函数
        
    return function_in

@function_out   #底层 ： login = function_out(login)
def login():
    print("开始登录")
    
# login = function_out(login)
login()