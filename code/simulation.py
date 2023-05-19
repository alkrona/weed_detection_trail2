#yahoo lets gooo
import model_of_weeder
import random
import field_generator
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
field2 = field_generator.field_generation(100)
path_of_traversal=[]
def path_allacator(path_of_traversal,field2):
    flag=0
    for i in range(100):
        if i%3==0:    
            if flag==0:
                for j in range(0,100):
                    path_of_traversal.append([i,j])
                flag=1
            elif flag==1:
                for j in range(99,-1):
                    path_of_traversal.append([i,j])
    return path_of_traversal
path_of_traversal=path_allacator(path_of_traversal,field2)

#for i in weed_location:
  #  print(i)
for i in weed_location:
    x_val = i[0]
    y_val = i[1]
    field[x_val][y_val]='w'



