class Car:
	def __init__(self, length, path):
		self.length = length
		self.path = path
		self.current = path[0]
		self.path_length = 0
	
	def car_sum(self,street_dict):
		s = 0
		for p in self.path:
			s += street_dict[p].length
		self.path_length = s 
