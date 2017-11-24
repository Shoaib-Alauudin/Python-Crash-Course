a = [1,2,3,4]
print(a)
print('%.2f'%123.44594965)
a = open('abcd.txt','w')
name = "Hello World This is a python code"
print(name.replace('e','77777'))
name.replace('H','777') # Do not work permanently (replace work for temporary)
print(type(name))
print(11//5)

'''
X       Y      Z            Result
True    True    True        Compiled
True    True    False       Compiled   (X OR Y) AND Z --> Failed
True    False   True        Compiled
True    False   False       Compiled
False   True    True        Compiled
False   True    False       Failed
False   False   True        Failed
False   False   False       Failed
'''
x = True
y = True
z = False
if (x or y) and z:
    print("Compiled")
else:
    print("Failed")


daysOfWeek = ['Monday',
              'Tuesday',
              'wENESDAY',
              'thursday',
              'friday',
              'saturday',
              'sunday']
months = ['jan',
          'feb',
          'march',
          'apr']
print("DaysOfWeek and Months"% months,daysOfWeek)
print("\x50" 'world' 'python')

class new:
    def __init__(self,number):
        self.id = number
        self.nameid = 6666

obj = new(125)
print(obj.id)
print(obj.nameid)
