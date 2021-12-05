#!/usr/bin/env python3

increases = 0

with open('lines') as file:
  list = enumerate(file)
  for idx, line in list:
    if idx == 0:
      last_item = line;
      continue

    if int(last_item) >= int(line):
      last_item = line
      continue

    increases += 1

    last_item = line;

print(increases)
