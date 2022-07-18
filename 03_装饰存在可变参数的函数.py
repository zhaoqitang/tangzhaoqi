def function_out(func):
    
    def fuction_in(*args, **kwargs):
        print("-----开始验证-----")   
        print("login:args=",*args)
        print("login:kwargs=", kwargs)
        #执行待装饰的函数
        #func((10,),{a:10})
        func(*args,**kwargs)  
    return fuction_in

#登录函数
@function_out 
#login = function_out(login)
def login(*args, **kwargs):
    print("开始登录 num = ")
    print("login:args=",*args)
    print("login:kwargs=", kwargs)
    

login(10,a=10)