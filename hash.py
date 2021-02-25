from car import Car
from intersection import Intersection
from streets import Street

def setup(street_dict, car_dict, int_dict):

	for c in car_dict:
		c.car_sum(street_dict)

	for i in int_dict.values():
		i.init()

def intersection_counts(street_dict, car_dict, int_dict):
	for car in car_dict:
		for p in car.path:
			int_num = street_dict[p].end
			inter = int_dict[int_num]
			idx = -1
			for i in range(len(inter.incoming)):
				if inter.incoming[i].name == p:
					idx = i		

			inter.counts[idx] += 1



inp = open('data/f.txt', 'r')
lines = inp.readlines()

initial_vars = lines[0]
initial_vars = initial_vars.split(" ")
total_seconds = int(initial_vars[0])
intersections = int(initial_vars[1])
streets = int(initial_vars[2])
cars = int(initial_vars[3])

lines = lines[1:]
street_list = lines[0:streets]
lines = lines[streets:]
car_list = lines[0:cars]


out = open('sol/f_sol.txt', 'w')
solution = []

inter_dic = {}
all_cars = []

street_dict = {}

# initialize inter dic
for i in range(intersections):
	inter_dic[i] = Intersection([], [], i)

for street in street_list:
	street_vars = street.split(" ")

	start = int(street_vars[0])
	end = int(street_vars[1]) 
	name = street_vars[2]
	length = int(street_vars[3])


	curr_street = Street(start, end, name, length)
	street_dict[name] = curr_street


	inter_dic[start].outgoing.append(curr_street)
	inter_dic[end].incoming.append(curr_street)


for car in car_list:
	car_vars = car.split(" ")
	#print(car_vars)
	length = int(car_vars[0])
	path = car_vars[1:length+1]
	path[-1] = path[-1].strip()
	all_cars.append(Car(length, path))



setup(street_dict, all_cars, inter_dic)
intersection_counts(street_dict, all_cars, inter_dic)


out.write(str(intersections))
out.write('\n')

for i in inter_dic.values():
	i.set_weights(i.counts)
	i.get_cycle_from_weights(out)

  

out.close()



