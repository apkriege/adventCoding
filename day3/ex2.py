lines = []

# read in file
with open('./data2.txt') as file:
  while (line := file.readline().rstrip()):
    lines.append(line)

def test (lines, idx, xx) :
  if idx < len(lines[0]) and len(lines) > 1 : 
    total = 0
    v = 0

    for a, line in enumerate(lines) : 
      total += int(line[idx])

    if xx == 'a' : 
      v = '1' if total >= len(lines) / 2 else '0'
    else : 
      v = '0' if total >= len(lines) / 2 else '1'

    newLines = []
    for a, line in enumerate(lines) :       
      if line[idx] == v :
        newLines.append(line)

    # print(newLines)

    idx += 1
    test(newLines, idx, xx)

  else : 
   print(int(lines[0],2))

test(lines, 0, 'a')
test(lines, 0, 'b')
