depth = 0
hrzntl = 0

with open('data') as file:
  list = enumerate(file)
  for idx, line in list:
    val = line.split()


    if val[0] == 'forward':
      hrzntl += int(val[1])
    
    elif val[0] == 'up':
      depth -= int(val[1])
    
    elif val[0] == 'down':
      depth += int(val[1])

print("Final {}".format(depth * hrzntl))

