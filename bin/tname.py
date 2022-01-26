#!/usr/bin/env python3

import glob
import linecache
import re
import sys


def main(args):

  if len(args) >= 1:
    test = args[0] #"../../Shopify/shopify/**/inventory_transfers_controller_test.rb:26"
    print(args)
    test_ids = test.split(":")

    if len(test_ids) != 2:
      print(f"Bad test spec: {test}")

    else:
      fnames = get_files(test_ids[0])
      if len(fnames) == 0:
        print(f"Test not found: {test}")

      elif len(fnames) == 1:
        line = linecache.getline(fnames[0], int(test_ids[1]))
        m = re.search("test \"(?P<desc>.*)\" do", line)
        if m:
          test_name = f"test_{re.sub(' ', '_', m.group('desc'))}"
          print(test_name)
        else:
          print(f"No test description found in line {test_ids[1]}:\n'{line[:-1]}'")

      else:
        print(f"Which file?")
        print(*fnames, sep = "\n")
  else:
    print("No test file given.")



def get_files(name):
  return glob.glob(name, recursive = True)

if __name__ == "__main__":
  main(sys.argv[1:])
