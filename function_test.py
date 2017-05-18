import numpy as np

def Conversion(array):  #converts 8 bit greyscale to 3 bit depth for 3d model
	row_count = 0
	item = 0
	for row in array:
		item = 0
		for pixel in row:
			if pixel < 32:
				array[row_count][item] =8
			elif pixel < 64:
				array[row_count][item] =7
			elif pixel < 96:
				array[row_count][item] =6
			elif pixel < 128:
				array[row_count][item] =5
			elif pixel < 160:
				array[row_count][item] =4
			elif pixel < 192:
				array[row_count][item] =3
			elif pixel < 224:
				array[row_count][item] =2
			else:
				array[row_count][item] =1
				print "i tried"
			item += 1
			print item
		row_count += 1
		print row
	return array

a = np.array([[1,2,3,4],
				[5,6,7,8],
				[9,10,11,12],
				[13,14,15,16]])

print Conversion(a)






