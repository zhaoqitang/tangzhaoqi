#装饰器：在不改变函数的代码前提下，给函数添加新的功能

#使用前提：
#1.存在闭包(用于扩展新的功能)   2.带扩展的普通函数(目的就是不改变该函数，还能增加新的功能 )

def function_out(func):
    #func = login
    def function_in():
        print("-----开始验证-----")
        #func() = login
        func()
    return function_in

@function_out     #@function_out 装饰了login()函数    底层：login = function_out(login)
def login():
    print("开始登录")
    
# #通过闭包调用外层函数
# login = function_out(login)   #这里login传参数传到func里面

login()       # #login() = function_in