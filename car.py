class Car:
  def __init__(self, length, path):
    self.length = length
    self.path = path
    self.current = path[0]
    self.path_length = 0


  def car_sum(street_dict):
	s = 0
	for p in path:
		s += street_dict[p].length
	c.path_length = 1/s 
