from car import Car
from intersection import Intersection
from streets import Street

inp = open('a.txt', 'r')
lines = inp.readlines()

initial_vars = lines[0]
initial_vars = initial_vars.split(" ")
total_seconds = initial_vars[0]
intersections = initial_vars[1]
streets = initial_vars[2]
cars = initial_vars[3]

lines = lines[1:]
street_list = lines[0:streets]
lines = lines[streets:]
car_list = lines[0:cars]


out = open('myfile.txt', 'w')
solution = []

inter_dic = {}


for street in street_list:
    street_vars = street.split(" ")

    start = street_vars[0]
    end = street_vars[1] 
    name = street_vars[2]
    length = street_vars[3]

    
    if street_vars[1] not in inter_dic: 
        inter_dic[] 

    
    

out.writelines(solution)
out.close()