def function_out(func):
    #func = login
    def function_in(num):
        print("-----开始验证-----")
        #func() = login
        return func(num)
    return function_in          #关键步骤 return

@function_out     #@function_out 装饰了login()函数    底层：login = function_out(login)
def login(num):
    print("开始登录")
    return num + 10              #关键步骤 return
    
# #通过闭包调用外层函数
# login = function_out(login)   #这里login传参数传到func里面
# #login() = function_in
result = login(8)
print(result)




#步骤：带装饰的函数必须有返回值(return)
#闭包的内层函数  func(*args,**kwargs)     改为   return func(*args,**kwargs) 