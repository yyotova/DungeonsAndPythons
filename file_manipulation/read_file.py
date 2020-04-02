from copy import deepcopy 
def read_from_file(file_name):
	level_array=[]
	treasures_list=[]
	file=open(file_name,"r")
	content=file.readlines()[:-1]
	for line in content:
		helper_list=[]
		for letter in range(0,len(line)):
			if line[letter]!="\n":
				helper_list.append(line[letter])
		level_array.append(helper_list)
	file.close()
	file=open(file_name,"r")
	treasure=file.readlines()[-1:]
	treasure=treasure[0][:-2]
	treasure=treasure[1::]
	# print(treasure)
	treasures_list=treasure.split(",")

	file.close()
	return level_array,treasures_list