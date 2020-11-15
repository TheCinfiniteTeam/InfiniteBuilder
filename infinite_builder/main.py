#encoding: utf-8
#导入库
from sys import builtin_module_names
import os, zipfile, sys, json, time, base64, socket, socketserver
import tkinter

class Build(object):#创建类
    def __init__(self):#创建初始化方法
        self.name = 'Infinite Builder Tool'#定义name
        self.id = 'infinite_builder_tool'#定义id
        self.version = 'b1'#定义版本
        self.runDir = os.getcwd()#定义运行路径

    def __str__(self):#如果以str输出会调用这个方法
        return self.name#返回一下软件名字

    def getInformation(self):#创建获取信息方法
        returnJson = { #创建信息字典
            'NAME': self.name,
            'ID': self.id,
            'VERSION': self.version,
            'RUN_DIR': self.runDir,
            'NOW_TIME': time.time()
        }
        return returnJson#返回信息字典

    def getHelpInformation(self):#创建获取帮助信息方法
        self.help = """
        -|*Infinite Builder Tool Help Information*|-
        Note: the use of this software caused by the user to bear, the author's team has no responsibility
        --------------------------------------------

        -|*无限构建工具帮助信息*|-
        注意:使用此软件造成的事物由使用者承担 作者团队无任何责任
        -------------------------
        """
        return self.help#返回帮助消息

    def comSelect(self):#创建选择方法
        return input('\n输入您要使用的功能\nEnter the function you want to use:')

    def comInitial(self):#创建初始化组件
        pass#TODO

    def comRunning(self):#创建运行组件
        pass#TODO
    
    def guiMode(self):#创建GUI(用户交互界面)模式
        self.guiClass = self.GUI()#创建窗口
        self.guiClass.gui()#调用gui方法

    def terminalMode(self):#定义终端(terminal)模式
        print(self.getHelpInformation())#打印帮助信息
        self.comSelect()#选择TODO

    def base64Icon(self):#创建生产ico方法
        with open(file='icon.ico',mode='wb') as imgIconFile:#使用with open创建icon.ico文件
            imgIconFile.write(base64.b64decode(open(file='icon_base64',encoding='utf-8').read()))#解析base64创建icon.ico文件

    class GUI(object):#创建GUI类
        def __init__(self):#创建初始化方法
            self.window = tkinter.Tk()#创建窗口
            self.window.iconbitmap('icon.ico')
            self.window.title('Infinite Budiler Tool')

        def gui(self):#创建gui方法
            self.window.mainloop()

    def runningPack(self,mode):#创建运行'整合包'
        self.base64Icon()
        if mode == 'terminal':#判断模式(mode)是否为terminal(终端)
            self.terminalMode()#调用Terminal(终端)模式
        elif mode == 'gui':#判断模式(mode)是否为gui(用户交互界面)
            self.guiMode()#调用GUI(用户交互界面)模式
        else:#否则判断
            raise ValueError("Type in Options but mode's value not == terminal or gui!")#报错 因为模式(mode)设置错误
if __name__ == "__main__":
    buildToolClass = Build()#实例化Build类

    buildToolClass.runningPack(mode='gui')#运行'整合包'
    
    os.remove('icon.ico')#移除图标文件清理缓存