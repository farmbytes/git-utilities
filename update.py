#!/usr/bin/env python

import os, sys, getopt

def main(argv):
   branchname = ''
   try:
      opts, args = getopt.getopt(argv,"hb:")
   except getopt.GetoptError:
      print 'update.py -b <branch-name>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'update.py -b <branch-name>'
         sys.exit()
      elif opt == '-b':
         branchname = arg
         os.system('git checkout ' + branchname)
         os.system('git pull')

if __name__ == "__main__":
    main(sys.argv[1:])
