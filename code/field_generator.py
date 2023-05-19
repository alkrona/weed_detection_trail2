# Define a class
import math
class Agri_field_element: # creating a field element
    def __init__(self, x_label=0, y_label=0, type_of='w',is_sprayed=0):
        self.x_label = x_label # x_axis grid location of the weed.
        self.y_label = y_label # y_axis grid location of the weed.
        self.type_of = type_of  # what kind of weed element is it, normal , weed or plant.
        self.is_sprayed = is_sprayed # weather or not the element has already been sprayed or not.

 
    def __repr__(self):
        return (f'Pokemon({self.power},'
                f'{self.level}, '
                f'{self.names})')
 
    def total_damage(self):
        return self.damage(self.power, self.level)
 
def field_generation(number_of_elements):
    arr=[]
    for i in range(number_of_elements/math.sqrt(number_of_elements)):
        for j in range(number_of_elements/math.sqrt(number_of_elements)):
            arr.append(Agri_field_element(i,j,"n",0))
    return arr


    