def biggest_by_index(lines, index):
  counter = [0, 0]

  for line in lines:
    x = int(str(line)[index])

    if x == 1:
      counter[0] += 1
    elif x == 0:
      counter[1] += 1

  return counter

with open('data') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    gamma = ""
    epsilon = ""

    for index in range(12):
      count = biggest_by_index(lines, index)
      
      gamma += str(count.index(min(count)))
      epsilon += str(count.index(max(count)))

    print("{}".format(int(gamma, 2) * int(epsilon, 2)))

