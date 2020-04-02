from file_manipulation.read_file import read_from_file 


def get_list_object(array,object):
	list_helper=[]	
	for i in range(0,len(array)):
		for j in range(0,len(array)):
			if self.level_array[i][j]==object:
				self.list_helper.append([i,j])

	return list_helper


class Dungeon:
	
	def __init__(self,file_name):
		self.level_array,self.treasures_list=read_from_file(file_name)
		self.spawn_location_list=[]
		self.obstacle_localtion=[]
		self.enemy_location=[]

	def get_obstacle_list(self):
		self.obstacle_localtion= get_list_object(self.level_array,"#")

	def get_spawn_location(self):
		self.spawn_location_list=get_list_object(self.level_array,"S")

	def spawn(self,hero):
		self.get_spawn_location()
		if len(self.spawn_location_list)==0:
			return False
		else:
			self.hero=hero
			self.hero_location=self.spawn_location_list[0]

