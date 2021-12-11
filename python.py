# variables
name = 'adam';
nums = [0, 59, 93]

# simple print
print(name)
print(name, nums)

# define function 
def test() :
    print ("test function")

# running function
test()

# for loop examples
for i, num in enumerate(nums) :
    print(num)

    # string output
    print('index {} in numbers is: {}'.format(str(i), num))

# object values
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

#object keys
for k in spam.keys():
    print(k)

# print full objects 
for i in spam.items():
    print(i)

# print object 
print(spam.get('color', 0))

# class student
class student : 
    def __init__(self, name): 
        self.name = name

stu = student('jim')
print(stu.name)