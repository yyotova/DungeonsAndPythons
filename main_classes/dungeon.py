import sys
sys.path.append('.')

from file_manipulation.read_file import read_from_file 
class Dungeon:
	
	def __init__(self,file_name):
			self.level_array,self.treasures_list=read_from_file(file_name)
			self.spawn_location_list=[]
	
	def get_spawn_location(self):
		for i in range(0,len(self.level_array)):
			for j in range(0,len(self.level_array)):
				if self.level_array[i][j]=="S":
					self.spawn_location_list.append([i,j])

	def spawn(self,hero):

		self.hero=hero	