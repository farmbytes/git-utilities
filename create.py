#!/usr/bin/env python

import os, sys, getopt

def main(argv):
   branchname = ''
   try:
      opts, args = getopt.getopt(argv,"he:n:")
   except getopt.GetoptError:
      print 'create.py -e <existing-branch> -n <new-branch>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'create.py -e <existing-branch> -n <new-branch>'
         sys.exit()
      elif opt == '-e':
         branchname = arg
         os.system('git stash')
         os.system('git checkout ' + branchname)
         os.system('git pull')
      elif opt == '-n':
         branchname = arg
         os.system('git checkout -b ' + branchname)
         os.system('git push -u origin ' + branchname)

if __name__ == "__main__":
    main(sys.argv[1:])
