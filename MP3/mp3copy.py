import os
import shutil

# song - author.mp3

class Check():
	def __init__(self):
		pass

	# check every name has ' -'
	def mp3_format(self, name):
		if name.find(" -") != -1:  # have " -"
			return True
		else:
			print(name + " without '-' ")  # print out the name without '-'

	def compare_length(self, string, target):
		name = string.strip(".mp3")
		name = name.split(" -")

		if (len(target) != len(name[0].strip())) and (len(target) != len(name[1].strip())):
			return False

	# find all .mp3
	def mp3file(self, dir):
		files = os.listdir(dir) # list all files

		# find .mp3
		namelist = []
		for f in files:
			name = f.find(".mp3")
			if name != -1:
				namelist.append(f)
		return namelist

	# get the string before '-'
	def getname(self, namelist):

		mp3list = []
		for mp3 in namelist:
			if self.mp3_format(mp3)==True:
				mp3name = mp3.rsplit(" -", 1)[0] # get name before '-'
				mp3list.append(mp3name.strip())

		return mp3list

	# find name in another dir
	def compare_dir(self, namelist, dir2):
		files = os.listdir(dir2)

		lostlist = []
		for name in namelist:
			cnt=0
			for f in files:
				result = f.find(name) # find the name in the mp3_path
				if result==-1:
					cnt=cnt+1
				else:
					if (self.compare_length(f,name)==False): # find the name and check string length
						#print(f)
						#print(name)
						cnt=cnt+1

			if cnt==len(files):
				lostlist.append(name)
		return lostlist

	# get all lost files' name
	def getlostname(self, dir, list):
		files = os.listdir(dir)

		newlist=[]
		for l in list:
			for f in files:
				songname = f.rsplit(" -", 1)[0]
				if l==songname.strip():
					newlist.append(f)
		return newlist

	# copy the lost files
	def copyfile(self, src, des, file):
		# Source path
		source = src+'/'+file

		# Destination path
		destination = des

		# Copy the content of
		# source to destination

		try:
			shutil.copy(source, destination)
			print("File copied successfully.")

		# If source and destination are same
		except shutil.SameFileError:
			print("Source and destination represents the same file.")

		# If destination is a directory.
		except IsADirectoryError:
			print("Destination is a directory.")

		# If there is any permission issue
		except PermissionError:
			print("Permission denied.")

		# For other errors
		except:
			print("Error occurred while copying file.")


# if __name__ == "__main__":
# 	mp3_path = "D:/mp3"
# 	file_path = "D:/test"
#
# 	namelist = mp3file(mp3_path)
# 	mp3list = getname(namelist)
# 	print(mp3list)
# 	lostlist = compare_dir(mp3list, file_path)
# 	print(lostlist)
#
# 	newlist = getlostname(mp3_path,lostlist)
# 	print(newlist)
#
# 	if newlist!="":
# 		for one in newlist:
# 			copyfile(mp3_path, file_path, one)


