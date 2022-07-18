"""  
1. 创建一个装饰器，一个带装饰的函数
2. 
"""
#定义一个让文字加粗的装饰器
def makeBlod(func):
    
    def function_in():
        return "<b>"+func()+"</b>"     #<b>helloworld-1</b>
    
    return function_in
#定义一个让文字倾斜的装饰器
def makeItalic(func):
    
    def function_in():
        return "<i>"+func()+"</i>"     #<i>helloworld-1</i>
    
    return function_in

# <b>helloworld-1   </b>作用:文字加粗    <b>是一个标签
@makeBlod
#test = makeBlod(test)
def text():
    return "helloworld-1"

@makeItalic
def text2():
    return "helloworld-2"

@makeItalic   #这边两个装饰，他就会打印<i><b>helloworld-3</b></i>
@makeBlod   #靠近函数的先执行，底层执行逻辑看图
def test3():
    return "helloworld-3"

print(text())
print(text2())
print(test3())