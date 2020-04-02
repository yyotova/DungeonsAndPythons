# import file_manipulation 


def get_list_object(array,object):
	list_helper=[]	
	for i in range(0,len(array)):
		for j in range(0,len(array)):
			if array[i][j]==object:
				list_helper.append([i,j])

	return list_helper

def check_for_something(points,array):
	for obstacle in array:
		if points[0]==obstacle[0] and points[1]==obstacle[1]:
			return True
	return False


class Dungeon:
	
	# def __init__(self,file_name):
	def __init__(self,map,treasures,enemy_list):
		# self.level_array,self.treasures_list=read_from_file(file_name)
		self.level_array=map
		self.treasures_list=treasures
		self.enemy_list=enemy_list
		self.spawn_location_list=[]
		self.obstacle_localtion=[]
		self.enemy_location=[]
		self.treasures_location=[]

		
	def get_obstacle_location(self):
		self.obstacle_localtion=get_list_object(self.level_array,"#")

	def get_treasure_location(self):
		self.enemy_location=get_list_object(self.level_array,"T")

	def get_enemy_location(self):
		self.enemy_location=get_list_object(self.level_array,"E")

	def get_spawn_location(self):
		self.spawn_location_list=get_list_object(self.level_array,"S")

	def fill_location_list(self):
		self.get_obstacle_location()
		self.get_enemy_location()
		self.get_spawn_location()
		self.get_treasure_location()

	def spawn(self,hero):
		self.get_spawn_location()
		if len(self.spawn_location_list)==0:
			return False
		else:
			self.hero=hero
			self.hero_location=self.spawn_location_list[0]
			self.put_hero_on_map()

	def print_map(self):
		for line in self.level_array:
			print(line)

	def move_hero(self,direction):
		# make them capital to ignore small or capital letter
		direction=direction.upper()
		# hero_location[x,y]
		# not using else because it looks better
		self.remove_hero_from_map() #remove hero from map
		
		if direction=="UP":
			self.hero_location[0]-=1
			if self.check_for_obstacles():
				self.hero_location[0]+=1
				# stops hero from going into walls

		elif direction=="DOWN":
			self.hero_location[0]+=1
			if self.check_for_obstacles():
				self.hero_location[0]-=1
				
		elif direction=="RIGHT":
			self.hero_location[1]+=1 
			if self.check_for_obstacles():
				self.hero_location[1]-=1

		elif direction=="LEFT":
			self.hero_location[1]-=1
			if self.check_for_obstacles():
				self.hero_location[1]+=1

		# move here put on map
		self.put_hero_on_map()
		# check for leaving level
		self.moving_out_of_bounds()

	def remove_hero_from_map(self):
		hero_point_x=self.hero_location[0]
		hero_point_y=self.hero_location[1]
		self.level_array[hero_point_x][hero_point_y]="."
		

	def put_hero_on_map(self):
		hero_point_x=self.hero_location[0]
		hero_point_y=self.hero_location[1]
		self.level_array[hero_point_x][hero_point_y]="H"

	def moving_out_of_bounds(self):
		hero_point_x=self.hero_location[0]
		hero_point_y=self.hero_location[1]
		if hero_point_x<0:
			self.move_hero("DOWN")
		if hero_point_x>len(self.level_array[hero_point_y]):
			self.move_hero("UP")
		if hero_point_y<0:
			self.move_hero("RIGHT")
		if hero_point_y>len(self.level_array):
			self.move_hero("LEFT")

	def check_for_obstacles(self):
		return check_for_something(self.hero_location,self.obstacle_localtion)

	def check_for_treasure(self):
		return check_for_something(self.hero_location,self.treasures_location)
		# get radom treasure
	
	def check_for_enemy(self):
		return check_for_something(self.hero_location,self.enemy_location)
		# fight now
