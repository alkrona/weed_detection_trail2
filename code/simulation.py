#yahoo lets gooo
import random
size_of_field =100 # it is the size of the field.
field = [['x' for i in range(size_of_field)] for i in range(size_of_field)]
for i in range(size_of_field):
    for j in range(size_of_field):
        field[i][j]='x'
for i in range(size_of_field):
    for j in range(size_of_field):
        pass
print(len(field))
print(len(field[0]))
for i in range(size_of_field):
    if(i%3==0):
        for j in range(size_of_field):
            field[i][j]='p'
weed_location=[]
for i in range(5):
    a1 =random.randrange(99)
    a2=random.randrange(99)
    weed_location.append([a1,a2])
#for i in weed_location:
  #  print(i)
for i in weed_location:
    x_val = i[0]
    y_val = i[1]
    field[x_val][y_val]='w'


