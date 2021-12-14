# base vars
lines = []
p = []
gammaStr = ''
epsilonStr = ''

# read in file
with open('./data2.txt') as file:
  while (line := file.readline().rstrip()):
    lines.append(line)

# set all base vals of p to 0
p = [0] * len(lines[0])

# add values to p
for i, line in enumerate(lines) :
  for j, l in enumerate(line) :
    p[j] += int(l)

# set gamma and epsilon strings
for i, x in enumerate(p) :
  gammaStr += '1' if p[i] > len(lines) / 2 else '0'
  epsilonStr += '1' if p[i] < len(lines) / 2 else '0'

# binary to int
gamma = int(gammaStr,2)
epsilon = int(epsilonStr,2)

print(gammaStr, gamma, epsilonStr, epsilon)
print(gamma * epsilon)
