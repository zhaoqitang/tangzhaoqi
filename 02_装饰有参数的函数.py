def function_out(func):
    
    def fuction_in(num):
        print("-----开始验证-----,num = ", num)   #这边加上num后还是报错
        #执行待装饰的函数
        func(num)  #要在这边加上num，因为login现在再func里   func(num) == login(num)
    return fuction_in

#登录函数
@function_out 
#login = function_out(login)
def login(num):
    print("开始登录 num = ",num)
    
# 装饰后，login == function_in  但是fuction_in中没有参数，所以报错
login(10)