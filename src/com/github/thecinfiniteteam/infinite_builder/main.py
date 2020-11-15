#encoding: utf-8
from sys import builtin_module_names
#from com.github.thecinfiniteteam.infinite_builder import *
import os, zipfile, sys, json, time, socket, socketserver

class Build(object):
    def __init__(self):
        self.name = 'Infinite Builder Tool'
        self.id = 'infinite_builder_tool'
        self.version = 'b1'
        self.runDir = os.getcwd()

    def __str__(self):
        return 'Infinite Builder Tool'

    def getInformation(self):
        returnJson = {
            'NAME': self.name,
            'ID': self.id,
            'VERSION': self.version,
            'RUN_DIR': self.runDir,
            'NOW_TIME': time.time()
        }
        return returnJson

    def getHelpInformation(self):
        self.help = """
        -|*Infinite Builder Tool Help Information*|-
        Note: the use of this software caused by the user to bear, the author's team has no responsibility
        --------------------------------------------

        -|*无限构建工具帮助信息*|-
        注意:使用此软件造成的事物由使用者承担 作者团队无任何责任
        -------------------------
        """
        return self.help

    def comInitial(self):
        pass

    def comRunning(self):
        pass

    def runningPack(self):
        print(self.getHelpInformation())

if __name__ == "__main__":
    buildToolClass = Build()

    buildToolClass.runningPack()