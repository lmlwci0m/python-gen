
class BasePythonFile(object):

    def __init__(self):
    
        self.imports = []
        self.inits = []
        self.body = []
    
        self.imports.append("#! /usr/bin/env python\n")
        self.imports.append("\n")
        self.imports.append("import sys\n")
        self.imports.append("import os\n")
        self.imports.append("import logging\n")
        self.imports.append("import argparse\n")
        self.imports.append("\n\n")
        
        self.inits.append("logging.basicConfig(level=logging.INFO)\n")
        self.inits.append("\n\n")
        
        self.body.append("if __name__ == '__main__':\n")
        self.body.append("    parser = argparse.ArgumentParser()\n")
        self.body.append("    #parser.add_argument('filepath')\n")
        self.body.append("    args = parser.parse_args()\n")
        self.body.append("    logging.info('Start')\n")
        
    def add_import(self, name):
        i = len(self.imports)
        self.imports[-1:-1] = ["import {0:s}\n".format(name)]
        
    def __iter__(self):
    
        for x in self.imports:
            yield x
            
        for x in self.inits:
            yield x
            
        for x in self.body:
            yield x