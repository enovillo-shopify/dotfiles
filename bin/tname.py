#!/usr/bin/env python3

import glob
import linecache
import re
import subprocess
import sys


def main(args):
  if len(args) >= 1:
    test_ids = args[0].split(":")

    if len(test_ids) != 2:
      print(f"Bad test spec: {args[0]}")

    else:
      fnames =glob.glob(f"**/{test_ids[0]}_test.rb", recursive = True)
      if len(fnames) == 0:
        print(f"Test not found: {test_ids[0]}")

      elif len(fnames) == 1:
        line = linecache.getline(fnames[0], int(test_ids[1]))
        m = re.search("test \"(?P<desc>.*)\" do", line)
        if m:
          test_name = f"test_{re.sub(' ', '_', m.group('desc'))}"
          command = f"dev test {fnames[0]} -n {test_name}"
          print(command)
          run_command(f"dev test {fnames[0]} -n {test_name}")
        else:
          print(f"No test description found in line {test_ids[1]}:\n'{line[:-1]}'")

      else:
        print(f"Which file?")
        print(*fnames, sep = "\n")
  else:
    print("No test file given.")


def run_command(command):
  result = subprocess.run(command, capture_output=True, text=True)
  # print(result)
  print(f"{result.stdout} {command[-1]}")
  print(result.stderr)


if __name__ == "__main__":
  main(sys.argv[1:])
