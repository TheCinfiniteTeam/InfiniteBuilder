#encoding: utf-8
#导入库
from sys import builtin_module_names
#from com.github.thecinfiniteteam.infinite_builder import *
import os, zipfile, sys, json, time, socket, socketserver

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

    def comInitial(self):#创建初始化组件
        pass#TODO

    def comRunning(self):#创建运行组件
        pass#TODO

    def runningPack(self):#创建运行'整合包'
        print(self.getHelpInformation())#打印帮助信息

if __name__ == "__main__":
    buildToolClass = Build()#实例化Build类

    buildToolClass.runningPack()#运行'整合包'