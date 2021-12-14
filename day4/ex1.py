lines = []

# read in file
# with open('./data.txt') as file:
#   while (line := file.readline().rstrip('\n')):
#     lines.append(line)
boards = []

file = open("./data.txt", "r")

lines = file.readlines()

for line in lines:
   if line == "\n":
    print("Empty Line")
   else:
    print(line.strip('\n'))

print(boards)
# print(lines)