#! /usr/bin/env python

import sys
import os
import logging
import argparse
from genutils.objgen import BasePythonFile


def parse():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-l", "--log", help="log level", type=str, choices=[
    'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    parser.add_argument("filepath", help="absolute path of the python file to create")
    
    return parser.parse_args()
    

def setup_log(args):
    if args.log:
        logging.basicConfig(level=getattr(logging, args.log.upper()))
    else:
        logging.basicConfig(level=logging.INFO)
        

if __name__ == '__main__':

    args = parse()
    
    setup_log(args)
        
    logging.info("Starting main generation...")
        
    with open(args.filepath, "w") as f:
    
        logging.info("File {0:s} opened for writing".format(args.filepath))
    
        base_file = BasePythonFile()
        base_file.add_import("twisted")
        base_file.add_import("wx")
    
        for line in base_file:
            f.write(line)
        
    logging.info("File {0:s} wrote succesfully".format(args.filepath))
        
    os.chmod(args.filepath, 0755)
    
    logging.info("File {0:s} permissions set succesfully".format(args.filepath))
    logging.info("Operation terminated without errors.".format(args.filepath))