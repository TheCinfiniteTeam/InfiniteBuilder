#encoding: utf-8
from com.github.thecinfiniteteam.infinite_builder import *
import os, zipfile, sys, json, time, socket, socketserver

class Build():
    def __init__(self):
        self.name = 'Infinite Builder Tool'
        self.id = 'infinite_builder_tool'
        self.version = 'b1'
        self.runDir = os.getcwd()
        self.pythonVersion = sys.version()

    def __str__(self):
        return 'Infinite Builder Tool'

    def getInformation(self):
        returnJson = {
            'NAME': self.name,
            'ID': self.id,
            'VERSION': self.version,
            'RUN_DIR': self.runDir,
            'PYTHON_VERSION': self.pythonVersion,
            'NOW_TIME': time.time()
        }
        return returnJson